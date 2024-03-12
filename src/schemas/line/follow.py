from typing import List
from pydantic import BaseModel


class Follow(BaseModel):
    isUnblocked: bool


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
    follow: Follow


class FollowWebHook(BaseModel):
    destination: str
    events: List[Event]