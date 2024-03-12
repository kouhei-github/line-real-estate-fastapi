from injector import inject, Module
from .rdbms_user import UserRDBMS

from .abstruct import AbstractUserDatabaseNotify
from schemas.index import UserAuth, UserOut
from models.index import User

class UserRepository(Module):
    @inject
    def __init__(self, repository: AbstractUserDatabaseNotify) -> None:
        if not isinstance(repository, AbstractUserDatabaseNotify):
            raise Exception("notify is not abstractTire.")
        self.repository = repository

    def register(self, line_id: str, email: str, password: str, url: str) -> UserOut:
        print("MySQlに応募者の情報を登録しました")
        user = UserAuth.parse_obj({
            "line_id": line_id,
            "email": email,
            "password": password,
            "image_url": url
        })
        return self.repository.save(user)

    def find_by_line_user_id(self, line_id: str) -> User:
        return self.repository.find_by_line_id(line_id)
class UserRepositoryModule(Module):
    def configure(self, binder):
        # binder.bind(AbstractNotify, to=SlackNotification)
        binder.bind(AbstractUserDatabaseNotify, to=UserRDBMS)