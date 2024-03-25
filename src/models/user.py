from sqlalchemy import Table, Integer, String, Column, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship
from config.index import Base

association_table = Table(
    'user_companies', Base.metadata,
    Column('company_id', Integer, ForeignKey('companies.id')),
    Column('user_id', Integer, ForeignKey('users.id')
)
                          )

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(250), nullable=True)
    line_user_id = Column(String(100))
    picture_url = Column(String(250))
    follow = Column(Boolean, default=True)
    companies = relationship("Company", secondary=association_table, back_populates="users")
    answer = relationship("Answer", back_populates="user")

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    line_id = Column(String(100))
    channel_access_token = Column(Text)
    message_id = Column(Integer, ForeignKey('messages.id'), nullable=True)
    message = relationship("Message", back_populates="companies")
    users = relationship("User", secondary=association_table, back_populates="companies")
    question = relationship("Question", back_populates="company")