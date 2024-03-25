from sqlalchemy import Integer, String, Column, ForeignKey, JSON, Text
from sqlalchemy.orm import relationship
from config.index import Base
class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True)
    content = Column(JSON)
    number = Column(Integer)

    question_id = Column(Integer, ForeignKey('questions.id'), nullable=True)
    question = relationship("Question", back_populates="answer")

    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    user = relationship("User", back_populates="answer")
