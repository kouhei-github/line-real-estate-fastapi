from schemas.index import FollowWebHook
from repositories.users.interface import UserRepositoryModule, UserRepository
from repositories.company.interface import CompanyRepositoryModule, CompanyRepository
from injector import Injector
from services.line_bot.core import CoreLineBot
from services.line_bot.message.text_message import TextMessage
from services.line_bot.message.quick_reply_postback_message import QuickReplyPostMessage

async def follow_use_case(body: FollowWebHook) -> str:
    print(body)

    # 会社
    company_injector = Injector([CompanyRepositoryModule()])
    company_repository = company_injector.get(CompanyRepository)
    company = await company_repository.find_by_line_user_id(body.destination)
    # line sdk
    bot = CoreLineBot(company.channel_access_token)

    # user
    profile = bot.get_profile(body.events[0].source.userId)
    injector = Injector([UserRepositoryModule()])
    _injection = injector.get(UserRepository)
    # 存在するか確認
    user = _injection.find_by_line_user_id(profile.user_id)
    if user is None:
        user = _injection.register(
            profile.user_id,
            profile.display_name,
            profile.picture_url,
            company.id
        )

    # メッセージの送信
    message = TextMessage(company.message)
    bot.send_message(body.events[0].source.userId, message)

    # 1つめの質問
    question = f"{user.name}さんの"
    if company.question[0]["type"] == "quickreply":
        question += company.question[0]["question"]
        items = [{"label": answer, "text": answer+"-1"} for answer in company.question[0]["answer"]]
        quick_reply_message = QuickReplyPostMessage(question, items)
        bot.send_message(body.events[0].source.userId, quick_reply_message)
    else:
        text_message = TextMessage(question+company.question[0]["question"])
        bot.send_message(body.events[0].source.userId, text_message)

    return body.events[0].source.userId
