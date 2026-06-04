from fastapi import FastAPI
from pydantic import BaseModel
from motivation import motivation_ai

app = FastAPI()

@app.get("/")
def home():
    return {
        "message":"Motivation API Running Successfully 🚀"
    }

class MotivationRequest(BaseModel):
    student_name: str
    weak_subject: str
    problem_solving: int
    stress_management: str
    backup_plan: str
    communication: str
    motivation_level: str

@app.post("/student-motivation")
def student_motivation(request: MotivationRequest):

    try:

        response = motivation_ai(
            request.student_name,
            request.weak_subject,
            request.problem_solving,
            request.stress_management,
            request.backup_plan,
            request.communication,
            request.motivation_level
        )

        return {
            "success": True,
            "motivation": response
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }