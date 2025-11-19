# routes/alumni_form_requests.py
from fastapi import APIRouter, HTTPException
from services.firestore_service import get_all, get_by_id, update_by_id
from models import AlumniFormRequestUpdate

router = APIRouter(prefix="/api/alumni-form-requests", tags=["alumni_form_requests"])

def response(success: bool, message: str, data=None, count: int = 0):
    return {"success": success, "message": message, "count": count, "data": data}

@router.get("/")
def list_requests():
    docs = get_all("Alumni_Form_Requests")
    return response(True, "Alumni form requests fetched", docs, len(docs))

@router.put("/{doc_id}")
def update_request(doc_id: str, payload: AlumniFormRequestUpdate):
    ok = update_by_id("Alumni_Form_Requests", doc_id, payload.dict(exclude_none=True))
    if not ok:
        raise HTTPException(status_code=404, detail="Request not found")
    doc = get_by_id("Alumni_Form_Requests", doc_id)
    return response(True, "Request updated successfully", doc, 1)
