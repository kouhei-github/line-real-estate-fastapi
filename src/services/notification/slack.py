from .abstruct import AbstractNotify

class SlackNotification(AbstractNotify):
    endpoint: str = "https://slack.com/api/chat.postMessage"
    message: str

    def send_message(self, message: str) -> str:
        print("Slackに送りました")
        return f"{self.endpoint}に{message}を送りました"