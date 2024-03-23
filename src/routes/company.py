from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from config.index import get_db
from schemas.index import CompanySchema, MessageSchema
from usecase.company.index import save_use_case, update_use_case

company = APIRouter(
    prefix="/api/company",
    tags=["Company"]
)

@company.post('/', status_code=status.HTTP_201_CREATED, summary="Create Line 追加")
async def create_company(data: CompanySchema, db: Session = Depends(get_db)):
    if data.line_id == "" or data.name == "" or data.channel_access_token == "":
        return Response(status_code=status.HTTP_400_BAD_REQUEST, content='{"message": "全て入力してください"}')

    response = await save_use_case(data)
    return {"status": 200}

@company.put('/{company_id}', status_code=status.HTTP_201_CREATED, summary="Create Line 追加")
async def update(company_id: int, data: MessageSchema, db: Session = Depends(get_db)):
    if data.message_id == "":
        return Response(status_code=status.HTTP_400_BAD_REQUEST, content='{"message": "全て入力してください"}')

    response = await update_use_case(company_id, data.message_id)
    return Response(status_code=status.HTTP_201_CREATED, content='{"message": "更新できました"}')
