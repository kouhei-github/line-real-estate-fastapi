from typing import List
from pydantic import BaseModel


class ContentProvider(BaseModel):
    type: str
    originalContentUrl: str
    previewImageUrl: str


class Message(BaseModel):
    id: str
    type: str
    quoteToken: str
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


class MessageMovieWebHook(BaseModel):
    destination: str
    events: List[Event]