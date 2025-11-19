# routes/events.py
from fastapi import APIRouter, HTTPException
from services.firestore_service import create_with_id, get_all, get_by_id
from models import EventCreate

router = APIRouter(prefix="/api/events", tags=["events"])

def response(success: bool, message: str, data=None, count: int = 0):
    return {"success": success, "message": message, "count": count, "data": data}

@router.post("/", status_code=201)
def create_event(payload: EventCreate):
    doc_id = payload.eventId
    body = payload.dict()
    body.pop("eventId", None)
    create_with_id("events", doc_id, body)
    return response(True, "Event created successfully", {"id": doc_id, **body}, 1)

@router.get("/")
def list_events():
    docs = get_all("events")
    return response(True, "Events fetched successfully", docs, len(docs))
