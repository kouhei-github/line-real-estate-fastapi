from .abstruct import AbstractNotify


class ChatworkNotification(AbstractNotify):
    endpoint: str = "https://chatwork.com/api/chat.postMessage"
    message: str

    def send_message(self, message: str) -> str:
        print("Chatworkに送りました")
        return f"{self.endpoint}に{message}を送りました"