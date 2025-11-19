# routes/admin.py
from fastapi import APIRouter, HTTPException
from services.firestore_service import create_with_id, get_by_id, update_by_id
from models import AdminCreate, AdminUpdate
from typing import Dict

router = APIRouter(prefix="/api/admin", tags=["admin"])

def response(success: bool, message: str, data=None, count: int = 0):
    return {"success": success, "message": message, "count": count, "data": data}

@router.post("/", status_code=201)
def create_admin(payload: AdminCreate):
    # use uid as doc id
    doc_id = payload.uid
    body: Dict = payload.dict()
    body.pop("uid", None)
    create_with_id("admin", doc_id, body)
    return response(True, "Admin created successfully", {"id": doc_id, **body}, 1)

@router.get("/{uid}")
def get_admin(uid: str):
    doc = get_by_id("admin", uid)
    if not doc:
        raise HTTPException(status_code=404, detail="Admin not found")
    return response(True, "Admin fetched successfully", doc, 1)

@router.put("/{uid}")
def update_admin(uid: str, payload: AdminUpdate):
    update_data = payload.dict(exclude_none=True)

    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="No valid fields provided for update"
        )

    ok = update_by_id("admin", uid, payload.dict(exclude_none=True))
    if not ok:
        raise HTTPException(status_code=404, detail="Admin not found")
    doc = get_by_id("admin", uid)
    return response(True, "Admin updated successfully", doc, 1)
