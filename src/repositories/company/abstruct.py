from abc import ABC, abstractmethod
from models.index import Company
from schemas.index import CompanySchema, CompanyMessageSchema

class AbstractCompanyDatabase(ABC):
    @abstractmethod
    def save(self, data: CompanySchema) -> dict:
        raise NotImplementedError()

    @abstractmethod
    def update_message(self, id: int, message_id: int) -> Company:
        raise NotImplementedError()

    @abstractmethod
    def find_by_line_id(self, line_id: str) -> CompanyMessageSchema:
        raise NotImplementedError()

    @abstractmethod
    def find_by_id(self, id: int) -> Company:
        raise NotImplementedError()