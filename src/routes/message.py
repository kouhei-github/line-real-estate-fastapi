from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from config.index import get_db
from schemas.index import MessageTextSchema
from usecase.message.index import save_message_use_case

message = APIRouter(
    prefix="/api/message",
    tags=["First Message"]
)

@message.post('/', status_code=status.HTTP_201_CREATED, summary="Create Line 追加")
async def create(data: MessageTextSchema, db: Session = Depends(get_db)):
    if data.text == "":
        return Response(status_code=status.HTTP_400_BAD_REQUEST, content='{"message": "全て入力してください"}')

    response = await save_message_use_case(data)
    return response