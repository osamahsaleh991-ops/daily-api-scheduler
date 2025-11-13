import requests
import os
from datetime import datetime

def make_api_call():
    url = "https://smmpanel.co/api/v2"
    
    # Get API key from environment variable
    api_key = os.environ.get('API_KEY')
    
    # Your API parameters (adjust based on your needs)
    payload = {
        'key': api_key,
        'action': 'balance',  # Example - change this to your actual action
        # Add other parameters as needed
    }
    
    try:
        response = requests.post(url, data=payload)
        print(f"[{datetime.now()}] Status: {response.status_code}")
        print(f"Response: {response.json()}")
        
        # Log success
        if response.status_code == 200:
            print("✓ API call successful")
        else:
            print(f"⚠ Warning: Unexpected status code")
            
    except Exception as e:
        print(f"✗ Error occurred: {e}")

if __name__ == "__main__":
    make_api_call()
