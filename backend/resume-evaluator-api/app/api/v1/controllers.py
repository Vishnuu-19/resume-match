from fastapi import APIRouter, HTTPException
from app.services.evaluate import evaluate
from app.services.suggestion import get_suggestions
from app.services.mock_interview import initiate_interview
from app.models.resume import Resume

router = APIRouter()

@router.post("/evaluate")
async def evaluate_resume(resume: Resume):
    score = evaluate(resume)
    if score > 80:
        return {"score": score, "suggestions": get_suggestions(score), "mock_interview": initiate_interview()}
    return {"score": score, "suggestions": get_suggestions(score)}

@router.get("/suggestions")
async def get_resume_suggestions(score: int):
    if score <= 100 and score >= 0:
        return get_suggestions(score)
    raise HTTPException(status_code=400, detail="Score must be between 0 and 100.")

@router.post("/mock-interview")
async def start_mock_interview(score: int):
    if score > 80:
        return initiate_interview()
    raise HTTPException(status_code=403, detail="Mock interview is only available for scores above 80%.")