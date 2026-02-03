import requests
import json

url = "http://localhost:8000/api/query"
data = {"query": "How many t-shirts are in stock?"}

print("Testing /api/query endpoint...")
print(f"URL: {url}")
print(f"Data: {data}")
print("-" * 60)

try:
    response = requests.post(url, json=data, timeout=30)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 200:
        result = response.json()
        print("\n✅ SUCCESS!")
        print(f"Answer: {result.get('answer', 'N/A')}")
    else:
        print("\n❌ ERROR!")
        
except Exception as e:
    print(f"\n❌ Exception: {e}")
    import traceback
    traceback.print_exc()
