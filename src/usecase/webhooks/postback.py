from schemas.index import SimplePostBackLineWebhook
from repositories.answer.interface import AnswerRepositoryModule, AnswerRepository
from injector import Injector
from repositories.company.interface import CompanyRepositoryModule, CompanyRepository
from services.line_bot.core import CoreLineBot
from services.line_bot.message.quick_reply_postback_message import QuickReplyPostMessage
from services.line_bot.message.text_message import TextMessage


async def postback_use_case(body: SimplePostBackLineWebhook) -> str:
    print(body)
    # 会社のIDと質問IDを取得
    company_injector = Injector([CompanyRepositoryModule()])
    company_repository = company_injector.get(CompanyRepository)
    company = await company_repository.find_by_line_user_id(body.destination)

    current_question = body.events[0].postback.data.split("-")
    question_num = current_question[1]
    answer = current_question[0]

    # 答え
    answer_injector = Injector([AnswerRepositoryModule()])
    answer_repository = answer_injector.get(AnswerRepository)
    _ = await answer_repository.save(
        answer,
        company.question_id,
        body.events[0].source.userId
    )
    bot = CoreLineBot(company.channel_access_token)

    text_message = TextMessage(f"ありがとうございます。{answer}ですね。")
    bot.send_message(body.events[0].source.userId, text_message)

    # line sdk
    profile = bot.get_profile(body.events[0].source.userId)
    # 質問愛用の抽出
    question = f"{profile.display_name}さんの"
    if company.question[int(question_num)]["type"] == "quickreply":
        question += company.question[int(question_num)]["question"]
        items = [{"label": answer, "text": answer+f"-{int(question_num)+1}"} for answer in company.question[int(question_num)]["answer"]]
        quick_reply_message = QuickReplyPostMessage(question, items)
        bot.send_message(body.events[0].source.userId, quick_reply_message)
    else:
        text_message = TextMessage(question+company.question[int(question_num)]["question"])
        bot.send_message(body.events[0].source.userId, text_message)
    return body.events[0].source.userId