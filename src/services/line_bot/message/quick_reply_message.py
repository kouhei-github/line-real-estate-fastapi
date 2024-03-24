from services.line_bot.message.abstruct import AbstractLineMessage
from typing import Dict, List
from linebot.models import TextSendMessage, QuickReply, QuickReplyButton, MessageAction

class QuickReplyMessage(AbstractLineMessage):
    def __init__(self, question: str, messages: List[Dict[str,str]]):
        self.question = question
        # クイックリプライのボタンを配置
        self.messages = messages

    def builder(self):
        items: List[QuickReplyButton] = []
        for message in self.messages:
            button =  QuickReplyButton(
                action=MessageAction(
                    label=message.get("label", ""),
                    text=message.get("text", "")
                )
            )
            items.append(button)
        return TextSendMessage(
            text=self.question,
            quick_reply=QuickReply(items=items)
        )