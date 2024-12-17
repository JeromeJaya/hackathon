import requests

def nvidia_api_query(prompt, api_key):
    url = "https://api.nvidia.com/genai/v1/chat"  # Replace with actual NVIDIA GenAI endpoint
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {"prompt": prompt}
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()
