# routes/alumni.py
from fastapi import APIRouter, HTTPException
from services.firestore_service import create_with_id, get_all, get_by_id, update_by_id, delete_by_id
from models import AlumniCreate, AlumniUpdate

router = APIRouter(prefix="/api/alumni", tags=["alumni"])

def response(success: bool, message: str, data=None, count: int = 0):
    return {"success": success, "message": message, "count": count, "data": data}

@router.post("/", status_code=201)
def create_alumni(payload: AlumniCreate):
    doc_id = payload.studentId
    body = payload.dict()
    body.pop("studentId", None)
    create_with_id("alumni", doc_id, body)
    return response(True, "Alumni created successfully", {"id": doc_id, **body}, 1)

@router.get("/")
def list_alumni():
    docs = get_all("alumni")
    return response(True, "Alumni fetched successfully", docs, len(docs))

@router.put("/{studentId}")
def update_alumni(studentId: str, payload: AlumniUpdate):
    ok = update_by_id("alumni", studentId, payload.dict(exclude_none=True))
    if not ok:
        raise HTTPException(status_code=404, detail="Alumni not found")
    doc = get_by_id("alumni", studentId)
    return response(True, "Alumni updated successfully", doc, 1)

@router.delete("/{studentId}")
def delete_alumni(studentId: str):
    ok = delete_by_id("alumni", studentId)
    if not ok:
        raise HTTPException(status_code=404, detail="Alumni not found")
    return response(True, "Alumni deleted successfully", None, 0)
