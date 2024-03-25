from abc import ABC, abstractmethod
from schemas.index import AnswerSchema, AnswerNumSchema

class AbstractAnswerDatabase(ABC):
    @abstractmethod
    def save(self, data: AnswerSchema) -> dict:
        raise NotImplementedError()

    @abstractmethod
    def rollback(self, question_id: int, user_id: str) -> AnswerNumSchema:
        raise NotImplementedError()

    @abstractmethod
    def find_by_question_id_and_line_user_id(self, question_id: int, user_id: str) -> AnswerNumSchema:
        raise NotImplementedError()

    @abstractmethod
    def finish(self, question_id: int, user_id: str):
        raise NotImplementedError()
