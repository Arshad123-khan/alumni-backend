# routes/student_data.py
from fastapi import APIRouter
from services.firestore_service import get_all

router = APIRouter(prefix="/api/student-data", tags=["student_data"])

def response(success: bool, message: str, data=None, count: int = 0):
    return {"success": success, "message": message, "count": count, "data": data}

@router.get("/", summary="Fetch all Student_Data_2016_2025 documents")
def get_student_data():
    docs = get_all("Student_Data_2016_2025")
    return response(True, "Student data fetched successfully", docs, len(docs))
