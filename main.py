import os
import firebase_admin
from firebase_admin import credentials
from google.cloud import firestore
from google.oauth2 import service_account
from fastapi import FastAPI
from dotenv import load_dotenv



# Load environment variables
load_dotenv()

app = FastAPI()

# Initialize Firebase
if not firebase_admin._apps:
    cred_path = os.getenv("FIREBASE_CREDENTIALS")
    firebase_cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(firebase_cred)
    print(" Firebase initialized successfully.")

google_cred = service_account.Credentials.from_service_account_file(cred_path)    
db = firestore.Client(credentials=google_cred)
print(" Firestore client created successfully.")

@app.get("/")
def root():
    return {"message": "Alumni API is running!"}

@app.get("/api/alumni")
def get_alumni():
    try:
        alumni_ref = db.collection("alumni") # Firestore collection name
        docs = alumni_ref.stream()
        
        alumni_list = [doc.to_dict() for doc in docs]
            
        return{"status": "success", "data": alumni_list}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
@app.get("/api/Alumni_Form_Requests")
def get_Alumni_Form_Requests():
    try:
        alumni_form_requests_ref = db.collection("Alumni_Form_Requests") # Firestore collection name
        docs = alumni_form_requests_ref.stream()
        
        alumni_form_requests_list = [doc.to_dict() for doc in docs]
            
        return{"status": "success", "data": alumni_form_requests_list}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
@app.get("/api/Student_Data_2016_2025")
def get_Student_Data_2016_2025():
    try:
        student_Data_2016_2025_ref = db.collection("Student_Data_2016_2025") # Firestore collection name
        docs = student_Data_2016_2025_ref.stream()
        
        student_Data_2016_2025_list = [doc.to_dict() for doc in docs]
            
        return{"status": "success", "data": student_Data_2016_2025_list}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
    
@app.get("/api/admin")
def get_admin():
    try:
        admin_ref = db.collection("admin") # Firestore collection name
        docs = admin_ref.stream()
        
        admin_list = [doc.to_dict() for doc in docs]
            
        return{"status": "success", "data": admin_list}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
    
@app.get("/api/events")
def get_events():
    try:
        events_ref = db.collection("events") # Firestore collection name
        docs = events_ref.stream()
        
        events_list = [doc.to_dict() for doc in docs]
            
        return{"status": "success", "data": events_list}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
    
@app.get("/api/file_upload_logs")
def get_file_upload_logs():
    try:
        file_upload_logs_ref = db.collection("file_upload_logs") # Firestore collection name
        docs = file_upload_logs_ref.stream()
        
        file_upload_logs_list = [doc.to_dict() for doc in docs]
            
        return{"status": "success", "data": file_upload_logs_list}
    except Exception as e:
        return {"status": "error", "message": str(e)}