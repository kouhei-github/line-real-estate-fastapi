from typing import List, Dict
from pydantic import BaseModel


class Postback(BaseModel):
    data: str
    params: Dict[str, str]


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
    postback: Postback


class PostBackDateTimeSelectWebHook(BaseModel):
    destination: str
    events: List[Event]