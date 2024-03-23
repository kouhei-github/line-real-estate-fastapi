from abc import ABC, abstractmethod
from models.index import Message
from schemas.index import MessageTextSchema

class AbstractMessageDatabase(ABC):
    @abstractmethod
    def save(self, data: MessageTextSchema) -> dict:
        raise NotImplementedError()

    @abstractmethod
    def find_by_id(self, id: int) -> Message:
        raise NotImplementedError()