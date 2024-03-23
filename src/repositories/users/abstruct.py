from abc import ABC, abstractmethod
from models.index import User, Company
from schemas.index import UserOut, UserAuth

class AbstractUserDatabaseNotify(ABC):
    @abstractmethod
    def save(self, data: UserAuth, company: Company) -> UserOut:
        raise NotImplementedError()

    @abstractmethod
    def find_by_line_id(self, line_id: str) -> User:
        raise NotImplementedError()