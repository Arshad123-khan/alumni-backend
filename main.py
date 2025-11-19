from fastapi import FastAPI
from firebase import db  # ensures firebase is initialized
from routes import admin, student_data, alumni, event_alumni, events, file_upload_logs, alumni_form_requests

app = FastAPI(title="Alumni Backend API")

# Include routers
app.include_router(admin.router)
app.include_router(student_data.router)
app.include_router(alumni.router)
app.include_router(event_alumni.router)
app.include_router(events.router)
app.include_router(file_upload_logs.router)
app.include_router(alumni_form_requests.router)

@app.get("/")
def root():
    return {"message": "Alumni API is running!"}

