from sqlalchemy import Integer, Text, Column
from sqlalchemy.orm import relationship
from config.index import Base

class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    text = Column(Text)
    companies = relationship("Company", back_populates="message")
