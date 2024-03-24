from pydantic import BaseModel

class CompanySchema(BaseModel):
    name: str
    line_id: str
    channel_access_token: str | None

class CompanyMessageSchema(BaseModel):
    id: int
    name: str
    message: str
    channel_access_token: str | None