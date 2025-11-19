import os
import firebase_admin
from firebase_admin import credentials
from google.cloud import firestore
from google.oauth2 import service_account
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Firebase
if not firebase_admin._apps:
    cred_path = os.getenv("FIREBASE_CREDENTIALS")
    firebase_cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(firebase_cred)
    print(" Firebase initialized successfully.")

# Create google-auth credentials for google-cloud client
google_cred = service_account.Credentials.from_service_account_file(cred_path)  

# Firestore client (using google-auth credentials)  
db = firestore.Client(credentials=google_cred)
print(" Firestore client created successfully.")