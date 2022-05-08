import requests
import json

def authenticate(request: dict):
    auth_type = request["auth"]
    url = request["url"]
    
    if auth_type == "none":
        r = requests.get(url)
        return r.json()
    

