#!/usr/bin/env python3
import requests
import json
from imports import compare,haschanged, fetch_keys
from log import do_log
import sys


#Test with real request on example json.
r = requests.get('https://jsonplaceholder.typicode.com/posts')
#r = requests.get('https://gorest.co.in/public/v2/posts/100/comments')

"""
The search takes an argument of an incoming response from the API you are using.
The old response gets stored locally to match against the new one for changes.

 """

def do_compare(json_data):
    """
    do_compare function, compares the new response with the old response stored in
    latestResponse.json

    :param: Any kind of json data.
    :return: A dict with added and removed keys. In the case the response has not changed
    it returns an empty dict
    
    """

    PATH_JSON = sys.path[0] + "/latestResponse.json"

    #Latest response from the API. Only looking at the keys. 
    latest_response_keys = fetch_keys.keys(json_data)
    
    #Stored API response.
    with open(PATH_JSON, "r") as file:
        data = json.loads(file.read())
        old_response_keys = fetch_keys.keys(data)
        file.close()

    #If something has been removed from the response.
    

    changed_keys = compare.key_compare(latest_response_keys,old_response_keys)

    with open("latestResponse.json", 'w') as file:
        file.write(json.dumps(r.json(), indent = 4))

    #return change_dict
    return changed_keys 




if __name__ == "__main__":
    """
    Runs the do_compare function that compares the old response with the new and
    looking for changes. 
    Ret
    """
    if haschanged.has_changed(do_compare(r.json())):

