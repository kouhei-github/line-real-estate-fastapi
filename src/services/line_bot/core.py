from linebot import LineBotApi
from services.line_bot.message.abstruct import AbstractLineMessage

class CoreLineBot:
    bot: LineBotApi
    def __init__(self, channel_token: str):
        self.channel_token = channel_token
        self.bot = LineBotApi(channel_token)

    def get_profile(self, user_id: str):
        return self.bot.get_profile(user_id)

    def send_message(self, user_id: str, message: AbstractLineMessage):
        if not isinstance(message, AbstractLineMessage):
            raise Exception("notify is not abstractTire.")
        self.bot.push_message(user_id, message.builder())
