from sqlalchemy import Integer, String, Column, ForeignKey, JSON, Text
from sqlalchemy.orm import relationship
from config.index import Base
class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    content = Column(JSON)
    number = Column(Integer)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=True)
    company = relationship("Company", back_populates="question")
    answer = relationship("Answer", back_populates="question")
