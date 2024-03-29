from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    id: int
    name: str | None
    email: str
    class Config:
        orm_mode = True
