from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes.index import (
    user,
    line,
    company,
    message,
    question,
)

from config.index import Base, engine

# テーブルを全て削除
# Base.metadata.drop_all(bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI()


# add Cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)
app.include_router(line)
app.include_router(company)
app.include_router(message)
app.include_router(question)
# app.include_router(health_check)