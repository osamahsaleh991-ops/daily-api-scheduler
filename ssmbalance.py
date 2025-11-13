import requests
import os
import sys
from datetime import datetime

def make_api_call():
    print(f"Python version: {sys.version}")
    print(f"Starting API call at {datetime.now()}")
    
    url = "https://smmpanel.co/api/v2"
    
    # Get API key
    api_key = os.environ.get('API_KEY')
    print(f"API_KEY present: {bool(api_key)}")
    print(f"API_KEY length: {len(api_key) if api_key else 0}")
    
    if not api_key:
        print("ERROR: API_KEY environment variable is not set!")
        sys.exit(1)
    
    # Prepare request
    payload = {
        'key': api_key,
        'action': 'balance'  # Change to your needed action
    }
    
    print(f"Sending request to: {url}")
    print(f"Payload keys: {list(payload.keys())}")
    
    try:
        response = requests.post(url, data=payload, timeout=30)
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        print(f"Response Text: {response.text}")
        
        # Try parsing JSON
        try:
            json_data = response.json()
            print(f"JSON Response: {json_data}")
        except ValueError as e:
            print(f"Could not parse as JSON: {e}")
        
        print("✓ API call completed successfully")
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Request Error: {type(e).__name__}: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Unexpected Error: {type(e).__name__}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    make_api_call()
