# models.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Admin
class AdminCreate(BaseModel):
    uid: str = Field(..., description="Custom UID to use as document id")
    email: str
    firstName: str
    lastName: str
    role: Optional[str] = None
    status: Optional[str] = None
    createdAt: Optional[str] = None  # ISO string (you can parse or store as-is)

class AdminUpdate(BaseModel):
    email: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    role: Optional[str] = None
    status: Optional[str] = None
    # updated fields don't require uid

# Alumni
class AlumniCreate(BaseModel):
    studentId: str = Field(..., description="Student ID used as document id")
    firstName: str
    lastName: str
    major: Optional[str]
    graduationYear: Optional[int]
    companyName: Optional[str]
    companyLocation: Optional[str]
    role: Optional[str]
    stillWorking: Optional[str]
    linkedURL: Optional[str]
    createdAt: Optional[datetime]
    lastUpdated: Optional[datetime]

class AlumniUpdate(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]
    major: Optional[str]
    graduationYear: Optional[int]
    companyName: Optional[str]
    companyLocation: Optional[str]
    role: Optional[str]
    stillWorking: Optional[str]
    linkedURL: Optional[str]
    lastUpdated: Optional[datetime]

# Alumni_Form_Requests
class AlumniFormRequestUpdate(BaseModel):
    company: Optional[str]
    companyLocation: Optional[str]
    degree: Optional[str]
    firstName: Optional[str]
    graduationYear: Optional[str]
    lastName: Optional[str]
    major: Optional[str]
    status: Optional[str]
    studentId: Optional[str]

# Student Data (only GET all requested)
# Event Alumni
class EventAlumniCreate(BaseModel):
    eventId: str = Field(..., description="Event ID to use as doc id or may be part of doc")
    studentId: str
    attended: bool
    feedbackScore: Optional[int]
    timestamp: Optional[datetime]

# Events
class EventCreate(BaseModel):
    eventId: str = Field(..., description="Event ID (used as document id)")
    eventTitle: str
    location: Optional[str]
    eventDate: Optional[datetime]
    createdAt: Optional[datetime]
    totalAttendees: Optional[int]
    totalSpeakers: Optional[int]
    totalVolunteers: Optional[int]
    year: Optional[int]

# File upload logs
class FileUploadLogCreate(BaseModel):
    id: str = Field(..., description="Log ID to use as document id")
    adminId: str
    fileName: str
    rowsProcessed: Optional[int]
    status: Optional[str]
    timeUploaded: Optional[datetime]

class FileUploadLogUpdate(BaseModel):
    adminId: Optional[str]
    fileName: Optional[str]
    rowsProcessed: Optional[int]
    status: Optional[str]
    timeUploaded: Optional[datetime]
