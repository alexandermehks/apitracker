import requests
import json

def authenticate(request: dict):
    auth_type = request["auth"]
    url = request["url"]
    
    if auth_type == "none":
        r = requests.get(url)
        return r.json()


    if auth_type == "basic":
        user = request["username"]
        password = request["password"]
        r = requests.get(url, auth=(user, password))
        print(r.json())
        return r.json()
        
    

