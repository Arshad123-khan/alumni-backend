🎓 Alumni Backend API (FastAPI + Firebase Firestore)

This repository contains the backend service for the Alumni Management System, built using:

FastAPI for REST APIs

Firebase Admin SDK for Firestore database

Modular route structure for enterprise-level scalability

The backend manages admins, alumni, events, student data, file logs, and alumni form requests.

🚀 Technologies Used

Python 3.10+

FastAPI

Uvicorn

Firebase Admin SDK

Pydantic

Firestore (NoSQL Database)

📁 Project Structure

alumni-backend/
│
├── main.py
├── models.py
├── utils/
│   └── firestore_helper.py
├── routes/
│   ├── admin.py
│   ├── alumni.py
│   ├── student_data.py
│   ├── events.py
│   ├── event_alumni.py
│   ├── file_upload_logs.py
│   ├── alumni_form_requests.py
│   └── __init__.py
├── serviceAccountKey.json   (IGNORED)
├── venv/                    (IGNORED)
├── .env                     (IGNORED)
└── README.md

🔐 Environment Setup

Create .env file in project root:
FIREBASE_CREDENTIALS=serviceAccountKey.json

Place your Firebase Admin key:
serviceAccountKey.json (but never push this file to GitHub)

▶️ Installation & Running the Server

1️⃣ Create virtual environment
python -m venv venv

2️⃣ Activate it
Windows
venv/Scripts/activate
Mac/Linux
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Start the server
uvicorn main:app --reload

🌐 Base API URL
http://localhost:8000/api/

📚 API Endpoints Summary

👨‍💼 Admin
| Method | Endpoint           | Description      |
| ------ | ------------------ | ---------------- |
| POST   | `/api/admin/`      | Create admin     |
| GET    | `/api/admin/{uid}` | Get admin by UID |
| PUT    | `/api/admin/{uid}` | Update admin     |
| GET    | `/api/admin/`      | Get all admins   |

🎓 Alumni
| Method | Endpoint                  | Description                       |
| ------ | ------------------------- | --------------------------------- |
| POST   | `/api/alumni/`            | Add alumni (requires `studentId`) |
| GET    | `/api/alumni/`            | Get all alumni                    |
| PUT    | `/api/alumni/{studentId}` | Update alumni                     |
| DELETE | `/api/alumni/{studentId}` | Delete alumni                     |

🧾 Student Data (2016–2025)
| Method | Endpoint             | Description          |
| ------ | -------------------- | -------------------- |
| GET    | `/api/student-data/` | Get all student data |

📅 Events
| Method | Endpoint       | Description    |
| ------ | -------------- | -------------- |
| POST   | `/api/events/` | Add event      |
| GET    | `/api/events/` | Get all events |

👥 Event Alumni
| Method | Endpoint             | Description             |
| ------ | -------------------- | ----------------------- |
| POST   | `/api/event-alumni/` | Add event-alumni record |
| GET    | `/api/event-alumni/` | Get all event-alumni    |

📤 File Upload Logs
| Method | Endpoint                 | Description            |
| ------ | ------------------------ | ---------------------- |
| POST   | `/api/file-logs/`        | Add file upload log    |
| GET    | `/api/file-logs/`        | Get all logs           |
| PUT    | `/api/file-logs/{logId}` | Update file upload log |

📝 Alumni Form Requests
| Method | Endpoint                       | Description                  |
| ------ | ------------------------------ | ---------------------------- |
| GET    | `/api/alumni-form/`            | Get all alumni form requests |
| PUT    | `/api/alumni-form/{requestId}` | Update form request          |


🧪 Testing APIs (Recommended: Postman)

Download:
https://www.postman.com/downloads/

For POST/PUT requests → use raw JSON body.
Use application/json as the body type.

🚫 Important Security Notes

Your .gitignore MUST contain:

venv/
__pycache__/
*.pyc
.env
*.json

This prevents accidentally uploading secrets like:

serviceAccountKey.json

.env

any credentials