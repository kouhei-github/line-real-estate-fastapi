from abc import ABC, abstractmethod
from schemas.index import QuestionSchema

class AbstractQuestionDatabase(ABC):
    @abstractmethod
    def save(self, data: QuestionSchema) -> dict:
        raise NotImplementedError()
