from typing import List
from pydantic import BaseModel


class VideoPlayComplete(BaseModel):
    trackingId: str


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
    videoPlayComplete: VideoPlayComplete


class MovieWatchCompleteWebHook(BaseModel):
    destination: str
    events: List[Event]