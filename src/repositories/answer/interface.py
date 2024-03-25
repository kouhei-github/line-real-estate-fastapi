from injector import inject, Module
from .rdbms import AnswerRDBMS
from typing import List
from .abstruct import AbstractAnswerDatabase
from schemas.index import AnswerSchema, AnswerNumSchema

class AnswerRepository(Module):
    @inject
    def __init__(self, repository: AbstractAnswerDatabase) -> None:
        if not isinstance(repository, AbstractAnswerDatabase):
            raise Exception("notify is not abstractTire.")
        self.repository = repository


    async def save(self, content: str, question_id: int, user_id: str) -> dict:
        print("MySQlに応募者の情報を登録しました")
        question = AnswerSchema.parse_obj({
            "content": content,
            "question_id": question_id,
            "user_id": user_id
        })
        return self.repository.save(question)

    async def back(self, question_id: int, user_id: str) -> AnswerNumSchema:
        return self.repository.rollback(question_id, user_id)

    async def find_by_question_id_and_line_user_id(self, question_id: int, line_user_id: str) -> AnswerNumSchema:
        return await self.repository.find_by_question_id_and_line_user_id(
            question_id, line_user_id
        )

class AnswerRepositoryModule(Module):
    def configure(self, binder):
        # binder.bind(AbstractNotify, to=SlackNotification)
        binder.bind(AbstractAnswerDatabase, to=AnswerRDBMS)