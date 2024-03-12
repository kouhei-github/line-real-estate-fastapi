from typing import Optional, List
from pydantic import BaseModel


class Mentionee(BaseModel):
    index: int
    length: int
    type: str
    userId: Optional[str]


class Mention(BaseModel):
    mentionees: List[Mentionee]


class Emoji(BaseModel):
    index: int
    length: int
    productId: str
    emojiId: str


class Message(BaseModel):
    id: str
    type: str
    quoteToken: str
    text: str
    emojis: Optional[List[Emoji]] = None
    mention: Optional[Mention] = None


class Source(BaseModel):
    type: str
    groupId: Optional[str] = None
    userId: str


class DeliveryContext(BaseModel):
    isRedelivery: bool


class Event(BaseModel):
    replyToken: str
    type: str
    mode: str
    timestamp: int
    source: Source
    webhookEventId: str
    deliveryContext: DeliveryContext
    message: Message


class MessageTextWebHook(BaseModel):
    destination: str
    events: List[Event]