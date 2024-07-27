import requests
import json

def clean(file_path, api_key):
    url = "https://your-api-endpoint/clean/"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    with open(file_path, 'rb') as file:
        files = {"file": file}
        response = requests.post(url, headers=headers, files=files)
    
    if response.status_code != 200:
        raise Exception(f"Failed to clean data: {response.text}")
    
    return response.json()
