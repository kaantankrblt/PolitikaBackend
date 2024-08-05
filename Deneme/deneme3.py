import os
from Gemini.settings import API_KEY
import google.generativeai as genai
import requests
from bs4 import BeautifulSoup

# Configure the Google Generative AI
genai.configure(api_key=API_KEY)

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    safety_settings=None,
    # See https://ai.google.dev/gemini-api/docs/safety-settings
)


# Function to extract main body text from a URL
def extract_body_text(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Try to find main content
        main_content = soup.find("main")
        if not main_content:
            main_content = soup.body

        paragraphs = main_content.find_all("p")
        body_text = " ".join(
            [para.get_text(separator=" ", strip=True) for para in paragraphs]
        )

        return body_text
    else:
        return "Failed to retrieve content"


# Function to summarize text using Google Generative AI
def summarize_text(text):
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(text)

    combined_response_text = ""
    for part in response.parts:
        combined_response_text += part.text

    return combined_response_text


# Example URL
url = "https://www.fdd.org/analysis/op_eds/2024/08/02/enough-is-enough-nato-must-suspend-cooperation-with-turkey/"

# Get the body text of the domain
text = extract_body_text(url)

# Summarize the extracted text
summary = summarize_text(text)

# Clear the console
os.system("clear")

# Print the summarized text
print("Summary:", summary)
