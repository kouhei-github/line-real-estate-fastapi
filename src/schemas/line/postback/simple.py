from pydantic import BaseModel
from typing import List
class Source(BaseModel):
    type: str
    userId: str

class DeliveryContext(BaseModel):
    isRedelivery: bool


class Postback(BaseModel):
    data: str


class Event(BaseModel):
    type: str
    postback: Postback
    webhookEventId: str
    deliveryContext: DeliveryContext
    timestamp: int
    source: Source
    replyToken: str
    mode: str


class SimplePostBackLineWebhook(BaseModel):
    destination: str
    events: List[Event]