from typing import List
from pydantic import BaseModel


class Things(BaseModel):
    deviceId: str
    type: str


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
    things: Things


class DeviceLinkWebHook(BaseModel):
    destination: str
    events: List[Event]