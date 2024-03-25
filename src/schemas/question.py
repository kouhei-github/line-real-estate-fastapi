from pydantic import BaseModel
from typing import List, Dict, Any

class QuestionSchema(BaseModel):
    content: List[Dict[str,Any]]
    company_id: int