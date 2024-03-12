from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int | None = None
    scopes: list[str] = []

class UserOut(BaseModel):
    email: str
    name: str | None
    id: int
    access_token: str
    refresh_token: str
    token_type: str

class UserAuth(BaseModel):
    email: str
    password: str
    line_id: str
    image_url: str