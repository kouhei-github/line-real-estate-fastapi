from typing import List
from pydantic import BaseModel


class Message(BaseModel):
    id: str
    type: str
    fileName: str
    fileSize: int


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


class MessageFileWebHook(BaseModel):
    destination: str
    events: List[Event]