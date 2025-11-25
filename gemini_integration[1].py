# gemini_integration.py
# Task 6: Google Gemini + Google Search memory-enabled chatbot (example template)
# NOTE: Replace YOUR_GEMINI_API_KEY and YOUR_SERPAPI_KEY with real keys.
# This is a template and requires internet and proper API keys to run.

import google.generativeai as genai
import requests

GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
SERP_API_KEY = "YOUR_SERPAPI_KEY"

genai.configure(api_key=GEMINI_API_KEY)

chat_memory = []

def google_search(query):
    url = f"https://serpapi.com/search?q={query}&api_key={SERP_API_KEY}"
    response = requests.get(url).json()
    try:
        return response["organic_results"][0]["snippet"]
    except Exception as e:
        return f"No live data found. ({e})"

def ask_gemini(user_msg):
    global chat_memory
    chat_memory.append({"role": "user", "message": user_msg})

    if "bitcoin" in user_msg.lower():
        live_data = google_search("Bitcoin price today")
        user_msg += f"\\n\\nLive Bitcoin Price: {live_data}"

    if "weather" in user_msg.lower():
        live_data = google_search("Weather in Mumbai")
        user_msg += f"\\n\\nLive Weather Update: {live_data}"

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(
        [{"role": m["role"], "parts": [m["message"]]} for m in chat_memory]
        + [{"role": "user", "parts": [user_msg]}]
    )

    bot_reply = response.text
    chat_memory.append({"role": "assistant", "message": bot_reply})
    return bot_reply

if __name__ == '__main__':
    print("AI Ready! Type 'exit' to quit.")
    while True:
        msg = input("You: ")
        if msg.lower() == "exit":
            break
        print("AI:", ask_gemini(msg))
