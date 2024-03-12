from typing import List, Optional
from pydantic import BaseModel


class ContentProvider(BaseModel):
    type: str


class ImageSet(BaseModel):
    id: str
    index: int
    total: int


class Message(BaseModel):
    type: str
    id: str
    quoteToken: str
    contentProvider: ContentProvider
    imageSet: Optional[ImageSet] = None


class Source(BaseModel):
    type: str
    userId: str


class DeliveryContext(BaseModel):
    isRedelivery: bool


class Event(BaseModel):
    type: str
    message: Message
    timestamp: int
    source: Source
    webhookEventId: str
    deliveryContext: DeliveryContext
    replyToken: str
    mode: str


class MessageImageWebHook(BaseModel):
    destination: str
    events: List[Event]
