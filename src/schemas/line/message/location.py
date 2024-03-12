from typing import List
from pydantic import BaseModel


class Message(BaseModel):
    id: str
    type: str
    title: str
    address: str
    latitude: float
    longitude: float


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


class MessageLocationWebHook(BaseModel):
    destination: str
    events: List[Event]