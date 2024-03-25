from injector import inject, Module
from .rdbms import QuestionRDBMS
from typing import List, Dict, Any
from .abstruct import AbstractQuestionDatabase
from schemas.index import QuestionSchema

class QuestionRepository(Module):
    @inject
    def __init__(self, repository: AbstractQuestionDatabase) -> None:
        if not isinstance(repository, AbstractQuestionDatabase):
            raise Exception("notify is not abstractTire.")
        self.repository = repository


    def save(self, content: List[Dict[str,Any]], company_id: int) -> dict:
        print("MySQlに応募者の情報を登録しました")
        question = QuestionSchema.parse_obj({
            "content": content,
            "company_id": company_id
        })
        return self.repository.save(question)

class QuestionRepositoryModule(Module):
    def configure(self, binder):
        # binder.bind(AbstractNotify, to=SlackNotification)
        binder.bind(AbstractQuestionDatabase, to=QuestionRDBMS)