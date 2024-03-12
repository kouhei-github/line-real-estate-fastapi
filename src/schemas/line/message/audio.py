from typing import List
from pydantic import BaseModel


class ContentProvider(BaseModel):
    type: str


class Message(BaseModel):
    id: str
    type: str
    duration: int
    contentProvider: ContentProvider


class Source(BaseModel):
    type: str
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


class MessageAudioWebHook(BaseModel):
    destination: str
    events: List[Event]