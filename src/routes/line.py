from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from config.index import get_db
from typing import Dict

from usecase.webhooks.index import (
    unfollow_use_case,
    follow_use_case,
    un_send_use_case,
    message_use_case,
)
from schemas.index import (
    UnFollowWebHook, FollowWebHook, UnSendWebHook
)

line = APIRouter(
    prefix="/api/line",
    tags=["Users"]
)


@line.post('/', status_code=status.HTTP_201_CREATED, summary="Create Line 追加")
async def create_user(data: Dict, db: Session = Depends(get_db)):
    event_type = data["events"][0]["type"]
    match event_type:
        case 'unfollow':
            body = UnFollowWebHook.parse_obj(data)
            await unfollow_use_case(body)
        case "follow":
            body = FollowWebHook.parse_obj(data)
            await follow_use_case(body)
        case "unsend":
            body = UnSendWebHook.parse_obj(data)
            await un_send_use_case(body)
        case "message":
            await message_use_case(data)
    return {"status": 200}