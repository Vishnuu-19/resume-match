from pydantic import BaseModel
from typing import List, Optional

class ResumeSchema(BaseModel):
    name: str
    email: str
    phone: str
    education: List[str]
    experience: List[str]
    skills: List[str]

class SuggestionSchema(BaseModel):
    suggestions: List[str]

class EvaluationResponseSchema(BaseModel):
    score: float
    suggestions: Optional[List[str]] = None
    mock_interview_available: bool = False