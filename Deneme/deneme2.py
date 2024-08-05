import os
from Gemini.settings import API_KEY
import google.generativeai as genai

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

chat_session = model.start_chat(history=[])

response = chat_session.send_message("Hi")

os.system("clear")

combined_response_text = ""
for part in response.parts:
    combined_response_text += part.text

print(combined_response_text)
