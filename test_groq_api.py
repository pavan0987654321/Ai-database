import os
from dotenv import load_dotenv
import requests

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

print("Testing Groq API Key...")
print(f"API Key: {groq_api_key[:20]}...{groq_api_key[-10:]}")
print("-" * 60)

# Test API call
url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {groq_api_key}",
    "Content-Type": "application/json"
}
data = {
    "model": "llama-3.3-70b-versatile",
    "messages": [
        {"role": "user", "content": "Say 'Hello' if you can hear me"}
    ],
    "max_tokens": 10
}

try:
    response = requests.post(url, headers=headers, json=data, timeout=10)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text[:500]}")
    
    if response.status_code == 200:
        print("\n✅ API Key is VALID and working!")
        result = response.json()
        print(f"AI Response: {result['choices'][0]['message']['content']}")
    elif response.status_code == 401:
        print("\n❌ API Key is INVALID or EXPIRED")
        print("Error: Authentication failed")
    elif response.status_code == 429:
        print("\n⚠️  Rate limit exceeded")
    else:
        print(f"\n❌ API Error: {response.status_code}")
        
except requests.exceptions.RequestException as e:
    print(f"\n❌ Network Error: {e}")
except Exception as e:
    print(f"\n❌ Error: {e}")
