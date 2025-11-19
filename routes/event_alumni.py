# routes/event_alumni.py
from fastapi import APIRouter, HTTPException
from services.firestore_service import create_with_id, get_all
from models import EventAlumniCreate

router = APIRouter(prefix="/api/event-alumni", tags=["event_alumni"])

def response(success: bool, message: str, data=None, count: int = 0):
    return {"success": success, "message": message, "count": count, "data": data}

@router.post("/", status_code=201)
def create_event_alumni(payload: EventAlumniCreate):
    # use eventId_studentId as custom doc id to avoid collisions (recommended)
    doc_id = f"{payload.eventId}_{payload.studentId}"
    body = payload.dict()
    create_with_id("event_alumni", doc_id, body)
    return response(True, "Event alumni record created", {"id": doc_id, **body}, 1)

@router.get("/")
def list_event_alumni():
    docs = get_all("event_alumni")
    return response(True, "Event alumni records fetched", docs, len(docs))
