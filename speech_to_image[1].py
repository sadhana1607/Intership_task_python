# speech_to_image.py
# Task 7: Speech-to-Image template
# NOTE: This template uses microphone speech recognition to get a prompt, then calls an image API.
# Replace YOUR_MONSTERA_KEY with your real API key and uncomment the requests code to run with internet.

import speech_recognition as sr
import requests

MONSTERA_API_KEY = "YOUR_MONSTERA_KEY"

def record_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak something...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except Exception as e:
        print("Could not understand audio:", e)
        return None

def generate_image(prompt):
    url = "https://clipdrop-api.co/text-to-image/v1"
    headers = {"x-api-key": MONSTERA_API_KEY}
    data = {"prompt": prompt}
    # response = requests.post(url, headers=headers, json=data)
    # if response.status_code == 200:
    #     with open("output_image.png", "wb") as f:
    #         f.write(response.content)
    #     print("✅ Image saved as output_image.png")
    # else:
    #     print("❌ Error:", response.text)
    print("This is a template. Replace API key and uncomment network code to call the image generation API.")

if __name__ == '__main__':
    prompt = record_speech()
    if prompt:
        generate_image(prompt)
