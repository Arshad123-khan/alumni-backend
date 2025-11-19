from typing import Optional, Dict, Any, List
from firebase import db

def get_all(collection: str) -> List[Dict[str,Any]]:
    docs = db.collection(collection).stream()
    return [{"id": d.id, **d.to_dict()} for d in docs]

def get_by_id(collection: str, doc_id: str) -> Optional[Dict[str, Any]]:
    doc = db.collection(collection).document(doc_id).get()
    if doc.exists:
        return {"id": doc.id, **doc.to_dict()}
    return None

def create_with_id(collection: str, doc_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
    db.collection(collection).document(doc_id).set(data)
    return {"id": doc_id, **data}

def update_by_id(collection: str, doc_id: str, data: Dict[str, Any]) -> bool:
    doc_ref = db.collection(collection).document(doc_id)
    if doc_ref.get().exists:
        doc_ref.update(data)
        return True
    return False

def delete_by_id(collection: str, doc_id: str) -> bool:
    doc_ref = db.collection(collection).document(doc_id)
    if doc_ref.get().exists:
        doc_ref.delete()
        return True
    return False