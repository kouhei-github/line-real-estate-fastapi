from typing import List
from pydantic import BaseModel


class Source(BaseModel):
    type: str
    userId: str


class DeliveryContext(BaseModel):
    isRedelivery: bool


class Event(BaseModel):
    type: str
    mode: str
    timestamp: int
    source: Source
    webhookEventId: str
    deliveryContext: DeliveryContext


class UnFollowWebHook(BaseModel):
    destination: str
    events: List[Event]