from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from config.index import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(250))
    password = Column(String(250))
    line_user_id = Column(String(100))
    picture_url = Column(String(250))