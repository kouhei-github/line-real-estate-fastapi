from injector import inject, Module
from .rdbms_message import MessageRDBMS

from .abstruct import AbstractMessageDatabase
from schemas.index import MessageTextSchema
from models.index import Message

class MessageRepository(Module):
    @inject
    def __init__(self, repository: AbstractMessageDatabase) -> None:
        if not isinstance(repository, AbstractMessageDatabase):
            raise Exception("notify is not abstractTire.")
        self.repository = repository


    def save(self, text: str) -> dict:
        print("MySQlにメッセージの情報を登録しました")
        message = MessageTextSchema(text=text)
        return self.repository.save(message)

    def find_by_line_user_id(self, message_id: int) -> Message:
        return self.repository.find_by_id(message_id)
class MessageRepositoryModule(Module):
    def configure(self, binder):
        # binder.bind(AbstractNotify, to=SlackNotification)
        binder.bind(AbstractMessageDatabase, to=MessageRDBMS)