#!/usr/bin/env python3
import requests
import json
import compare,haschanged, fetch_keys
from logs.log import do_log
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
    latestResponse.json. This is the function that runs the check.

    :param: Any kind of json data.
    :return: A dict with added and removed keys. In the case the response has not changed
    it returns an empty dict
    
    """
    #This is the relative path to the JSON file to store the latest response.
    PATH_JSON = "latestResponse.json"

    #Latest response from the API. Only looking at the keys. 
    latest_response_keys = fetch_keys.keys(json_data)
    
    #Stored API response.
    with open(PATH_JSON, "r") as file:
        data = json.loads(file.read())
        old_response_keys = fetch_keys.keys(data)
        file.close()

    changed_keys = compare.key_compare(latest_response_keys,old_response_keys)

    with open("latestResponse.json", 'w') as file:
        file.write(json.dumps(r.json(), indent = 4))
    return changed_keys 

if __name__ == "__main__":
    """
    Runs the do_compare function that compares the old response with the new and
    looking for changes. 
    Ret
    """
    compared = do_compare(r.json())
    if haschanged.has_changed(compared):
        do_log(compared)
        #TODO: => Add email, SMS, slack?
        pass
