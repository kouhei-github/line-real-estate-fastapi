from linebot.models import TextSendMessage
from services.line_bot.message.abstruct import AbstractLineMessage

class TextMessage(AbstractLineMessage):
    def __init__(self, message: str):
        self.text = message

    def builder(self):
        return TextSendMessage(self.text)