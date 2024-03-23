from .abstruct import AbstractMessageDatabase
from models.index import Message
from config.index import get_db
from sqlalchemy.orm import Session
from schemas.index import MessageTextSchema
from services.jwt_token import create_access_token, verify_password, create_refresh_token, get_hashed_password

class MessageRDBMS(AbstractMessageDatabase):
    def __init__(self):
        self.db: Session = next(get_db())

    def save(self, data: MessageTextSchema) -> dict:
        message = Message(
            text=data.text
        )

        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)
        return {"message": "Company created"}

    def find_by_id(self, id: int) -> Message:
        record = self.db.query(Message).filter(Message.id == id).first()
        self.db.close()
        return record