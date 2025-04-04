import requests
import json
import time

# Test only the QR code endpoint
URL = "http://127.0.0.1:5000/generate_qrcode"
PAYLOAD = {
    "data": "https://example.com",
    "is_dynamic": False
}
HEADERS = {"Content-Type": "application/json", "X-CSRFToken": ""}

print(f"Testing QR code endpoint: {URL}")
print(f"Payload: {json.dumps(PAYLOAD)}")
print(f"Headers: {HEADERS}")

# Try the request
try:
    response = requests.post(URL, json=PAYLOAD, headers=HEADERS, timeout=15)
    print(f"Status code: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 200:
        data = response.json()
        if "image_url" in data:
            image_url = data["image_url"]
            img_response = requests.get(f"http://127.0.0.1:5000{image_url}")
            print(f"Image URL: http://127.0.0.1:5000{image_url}")
            print(f"Image fetch status: {img_response.status_code}")
except Exception as e:
    print(f"Exception occurred: {str(e)}")
    
print("Test completed.") 