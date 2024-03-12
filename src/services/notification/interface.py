from injector import inject, Module
from .slack import SlackNotification
from .chatwork import ChatworkNotification
from .abstruct import AbstractNotify


class ApplyRegister:
    @inject
    def __init__(self, notify: AbstractNotify) -> None:
        if not isinstance(notify, AbstractNotify):
            raise Exception("notify is not abstractTire.")
        self.notify = notify

    def register(self, message: str) -> None:
        print("DynamoDBに応募者の情報を登録しました")
        print(self.notify.send_message(message))

class ApplyRegisterModule(Module):
    def configure(self, binder):
        # binder.bind(AbstractNotify, to=SlackNotification)
        binder.bind(AbstractNotify, to=ChatworkNotification)