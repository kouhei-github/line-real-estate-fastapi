from pydantic import BaseModel

class MessageSchema(BaseModel):
    message_id: int

class MessageTextSchema(BaseModel):
    text: str