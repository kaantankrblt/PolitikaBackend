import os
import json
import firebase_admin
from firebase_admin import credentials, firestore
import google.generativeai as genai
from settings import API_KEY

# Path to your JSON file
JSON_FILE_PATH = "Political_news.json"
SERVICE_ACCOUNT_PATH = "/Users/kaantankarabulut/Desktop/Developer/WebFetching/politika-13050-firebase-adminsdk-kg4xy-1244cca38f.json"

PROMPT = "Never give me a title or header or etc. always pure text. With these informations give the brief of political news. dont make headlines and dont cut paragraps. just give me the text. dont make sections. give all news together. make a paragraph that explain every news and give a brief. make sure you give every news."
MODEL = "gemini-pro"


# Function to load JSON and filter required fields
def load_json_data(file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        # Extract only title and description
        filtered_data = [
            {"title": item["title"], "description": item["description"]}
            for item in data
        ]
        return filtered_data
    except FileNotFoundError:
        print(f"Error: JSON file not found at {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}")
        return None
    except KeyError as e:
        print(f"Error: Missing expected key {e} in JSON data")
        return None


# Load the JSON data
json_data = load_json_data(JSON_FILE_PATH)

if json_data is not None:
    prompt = PROMPT.format(json.dumps(json_data))
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(MODEL)
    response = model.generate_content(prompt)

    os.system("clear")
    combined_response_text = ""
    for part in response.parts:
        combined_response_text += part.text

    print(combined_response_text)

    # Initialize the Firebase Admin SDK
    cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    # Reference to your Firestore collection
    doc_ref = db.collection("Gemini_news_summary").document("Politics")

    # Upload the generated content
    doc_ref.set({"brief": combined_response_text})
    print("Generated content uploaded to Firestore successfully.")
else:
    print("No data to upload.")
