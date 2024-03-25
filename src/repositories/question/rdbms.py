from .abstruct import AbstractQuestionDatabase
from models.index import Question
from config.index import get_db
from sqlalchemy.orm import Session
from schemas.index import QuestionSchema

class QuestionRDBMS(AbstractQuestionDatabase):
    def __init__(self):
        self.db: Session = next(get_db())

    def save(self, data: QuestionSchema) -> dict:
        question = Question(
            content=data.content,
            number=len(data.content),
            company_id=data.company_id
        )


        self.db.add(question)
        self.db.commit()
        self.db.refresh(question)
        return {"message": "question created"}