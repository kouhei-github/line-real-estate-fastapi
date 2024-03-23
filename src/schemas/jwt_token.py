from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int | None = None
    scopes: list[str] = []

class UserOut(BaseModel):
    email: str | None
    name: str
    id: int
    access_token: str
    refresh_token: str
    token_type: str

class CompanySchema(BaseModel):
    name: str
    line_id: str

class UserAuth(BaseModel):
    name: str
    line_id: str
    image_url: str
    follow: bool
