from schemas.index import MessageTextWebHook
from injector import Injector
from repositories.company.interface import CompanyRepositoryModule, CompanyRepository
from repositories.answer.interface import AnswerRepositoryModule, AnswerRepository
from services.line_bot.core import CoreLineBot
from services.line_bot.message.quick_reply_message import QuickReplyMessage
from services.line_bot.message.quick_reply_postback_message import QuickReplyPostMessage
from services.line_bot.message.text_message import TextMessage


async def text_message(body: MessageTextWebHook) -> str:
    print(body.events[0].message.text)

    # 最終問題答え済みだったらreturn
    company_injector = Injector([CompanyRepositoryModule()])
    company_repository = company_injector.get(CompanyRepository)
    company = await company_repository.find_by_line_user_id(body.destination)

    # 答え
    answer_injector = Injector([AnswerRepositoryModule()])
    answer_repository = answer_injector.get(AnswerRepository)
    answer = await answer_repository.find_by_question_id_and_line_user_id(company.question_id, body.events[0].source.userId)
    bot = CoreLineBot(company.channel_access_token)
    profile = bot.get_profile(body.events[0].source.userId)

    if body.events[0].message.text == "はい":
        # 次の質問に行く
        if answer.current_num == company.max:
            if answer.is_finish: return ""
            question = "最終確認です。以下でよろしいでしょうか？"
            items = [{"label": "はい", "text": "はい"}, {"label": "いいえ", "text": "いいえ"}]
            quick_reply_message = QuickReplyMessage(question, items)
            bot.send_message(body.events[0].source.userId, quick_reply_message)

            # 自動応答を終了させる
            await answer_repository.finish(company.question_id, body.events[0].source.userId)

            return ""
        question = f"{profile.display_name}さんの"
        if company.question[int(answer.current_num)]["type"] == "quickreply":
            question += company.question[int(answer.current_num)]["question"]
            items = [{"label": answer, "text": answer + f"-{int(answer.current_num) + 1}"} for answer in
                     company.question[int(answer.current_num)]["answer"]]
            quick_reply_message = QuickReplyPostMessage(question, items)
            bot.send_message(body.events[0].source.userId, quick_reply_message)
        else:
            text_message = TextMessage(question + company.question[int(answer.current_num)]["question"])
            bot.send_message(body.events[0].source.userId, text_message)

        return ""
    elif body.events[0].message.text == "いいえ":
        question = f"{profile.display_name}さんの"

        answer = await answer_repository.back(company.question_id, body.events[0].source.userId)
        if company.question[int(answer.current_num)]["type"] == "quickreply":
            question += company.question[int(answer.current_num)-1]["question"]
            items = [{"label": answer, "text": answer + f"-{int(answer.current_num)}"} for answer in
                     company.question[int(answer.current_num)]["answer"]]
            quick_reply_message = QuickReplyPostMessage(question, items)
            bot.send_message(body.events[0].source.userId, quick_reply_message)
        else:
            text_message = TextMessage(question + company.question[int(answer.current_num)]["question"])
            bot.send_message(body.events[0].source.userId, text_message)
        return ""

    _ = await answer_repository.save(
        body.events[0].message.text,
        company.question_id,
        body.events[0].source.userId
    )

    question = f"「{body.events[0].message.text}」でよろしいですか？"
    items = [{"label": "はい", "text": "はい"}, {"label": "いいえ", "text": "いいえ"}]
    quick_reply_message = QuickReplyMessage(question, items)
    bot.send_message(body.events[0].source.userId, quick_reply_message)
    return body.events[0].source.userId