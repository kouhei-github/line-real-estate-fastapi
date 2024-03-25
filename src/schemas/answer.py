from pydantic import BaseModel
from typing import List, Dict, Any

class AnswerSchema(BaseModel):
    content: str
    question_id: int
    user_id: str

class AnswerNumSchema(BaseModel):
    current_num: int

class AnswerBackSchema(BaseModel):
    question_id: int
    user_id: str
