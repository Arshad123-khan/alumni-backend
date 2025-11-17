import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

#Get the path of firebase credentials JSON
cred_path =  os.getenv("FIREBASE_CREDENTIALS")

# Initializing Firebase app if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)
    
# Get Firestore client
db = firestore.client()