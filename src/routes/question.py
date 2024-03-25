from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from config.index import get_db
from schemas.index import QuestionSchema
from usecase.question.index import save_use_case

question = APIRouter(
    prefix="/api/question",
    tags=["Question"]
)

@question.post('/', status_code=status.HTTP_201_CREATED, summary="Create Line 追加")
async def create(data: QuestionSchema, db: Session = Depends(get_db)):
    if len(data.content) == 0:
        return Response(status_code=status.HTTP_400_BAD_REQUEST, content='{"message": "全て入力してください"}')

    return await save_use_case(data)