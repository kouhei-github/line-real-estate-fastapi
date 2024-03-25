import json

from .abstruct import AbstractAnswerDatabase
from models.index import Answer, User
from config.index import get_db
from sqlalchemy.orm import Session
from schemas.index import AnswerSchema, AnswerNumSchema

class AnswerRDBMS(AbstractAnswerDatabase):
    def __init__(self):
        self.db: Session = next(get_db())

    def save(self, data: AnswerSchema) -> dict:

        user = self.db.query(User).filter(User.line_user_id == data.user_id).first()

        answer = self.db.query(Answer).filter(Answer.user_id == user.id).filter(Answer.question_id == data.question_id).first()
        if answer is None:
            answer = Answer(
                content=[data.content],
                number=1,
                question_id=data.question_id,
                user_id=user.id
            )
            self.db.add(answer)
        else:
            answer.content = answer.content + [data.content]
            answer.number=len(answer.content)

        self.db.commit()
        self.db.refresh(answer)
        return {"message": "question created"}

    def rollback(self, question_id: int, user_id: str) -> AnswerNumSchema:
        user = self.db.query(User).filter(User.line_user_id == user_id).first()

        answer = self.db.query(Answer).filter(Answer.user_id == user.id).filter(
            Answer.question_id == question_id).first()

        record = list(answer.content)  # 現在のリストをコピーします
        record.pop()
        answer.content = record
        answer.number = len(record)

        self.db.commit()
        self.db.refresh(answer)
        return AnswerNumSchema(current_num=answer.number)

    async def find_by_question_id_and_line_user_id(self, question_id: int, user_id: str):
        user = self.db.query(User).filter(User.line_user_id == user_id).first()

        answer = self.db.query(Answer).filter(Answer.user_id == user.id).filter(
            Answer.question_id == question_id).first()

        return AnswerNumSchema(current_num=answer.number)
