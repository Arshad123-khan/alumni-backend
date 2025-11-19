# routes/file_upload_logs.py
from fastapi import APIRouter, HTTPException
from services.firestore_service import create_with_id, get_all, get_by_id, update_by_id
from models import FileUploadLogCreate, FileUploadLogUpdate

router = APIRouter(prefix="/api/file-upload-logs", tags=["file_upload_logs"])

def response(success: bool, message: str, data=None, count: int = 0):
    return {"success": success, "message": message, "count": count, "data": data}

@router.get("/")
def list_logs():
    docs = get_all("file_upload_logs")
    return response(True, "File upload logs fetched", docs, len(docs))

@router.get("/{log_id}")
def get_log(log_id: str):
    doc = get_by_id("file_upload_logs", log_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Log not found")
    return response(True, "Log fetched", doc, 1)

@router.post("/", status_code=201)
def create_log(payload: FileUploadLogCreate):
    doc_id = payload.id
    body = payload.dict()
    body.pop("id", None)
    create_with_id("file_upload_logs", doc_id, body)
    return response(True, "Log created successfully", {"id": doc_id, **body}, 1)

@router.put("/{log_id}")
def update_log(log_id: str, payload: FileUploadLogUpdate):
    ok = update_by_id("file_upload_logs", log_id, payload.dict(exclude_none=True))
    if not ok:
        raise HTTPException(status_code=404, detail="Log not found")
    doc = get_by_id("file_upload_logs", log_id)
    return response(True, "Log updated successfully", doc, 1)
