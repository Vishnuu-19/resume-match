from fastapi import APIRouter, HTTPException
from app.api.v1.controllers import evaluate_resume, get_suggestions, initiate_mock_interview
from app.api.v1.schemas import ResumeSchema, SuggestionSchema

router = APIRouter()

@router.post("/evaluate", response_model=dict)
async def evaluate(resume: ResumeSchema):
    score = await evaluate_resume(resume)
    if score > 80:
        return {"score": score, "mock_interview": True}
    return {"score": score, "mock_interview": False}

@router.get("/suggestions", response_model=SuggestionSchema)
async def suggestions(score: int):
    if score <= 0:
        raise HTTPException(status_code=400, detail="Invalid score")
    return await get_suggestions(score)

@router.post("/mock-interview")
async def mock_interview(resume: ResumeSchema):
    score = await evaluate_resume(resume)
    if score > 80:
        return await initiate_mock_interview(resume)
    raise HTTPException(status_code=403, detail="Score must exceed 80% for mock interview")