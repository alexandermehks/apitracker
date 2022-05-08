#!/usr/bin/env python3
import requests
import json
from helpers import compare,haschanged,fetch_keys, authentication
from logs.log import do_log
import sys,os, os.path



#Test with real request on example json.
r = requests.get('https://jsonplaceholder.typicode.com/posts')
#r = requests.get('https://gorest.co.in/public/v2/posts/100/comments')

"""
The search takes an argument of an incoming response from the API you are using.
The old response gets stored locally to match against the new one for changes.

 """

def do_compare():
    """
    do_compare function, compares the new response with the old response stored in
    latestResponse.json. This is the function that runs the check.

    :param: Any kind of json data.
    :return: A dict with added and removed keys. In the case the response has not changed
    it returns an empty dict
    
    """

    with open("endpoints.json", "r") as file:
        endpoints = json.loads(file.read())
        file.close()

    for a in endpoints:
        striped_url = a["url"].replace("/","")
        PATH_JSON = f"responses/{striped_url}.json"
        latest_response = authentication.authenticate(a)
        latest_response_keys = fetch_keys.keys(latest_response)

        """
        If the file exists, we read the data from it.
        If not, we create it and dumps the response in it.
        """
        if os.path.exists(PATH_JSON):
            with open(PATH_JSON, "r") as file:
                data = json.loads(file.read())
                old_response_keys = fetch_keys.keys(data)
                file.close()
        else:
            with open(PATH_JSON,'w') as file:
                file.write(json.dumps(latest_response, indent = 4))
                old_response_keys = latest_response_keys
                file.close()
        
        changed_keys = compare.key_compare(latest_response_keys, old_response_keys)

        with open(PATH_JSON,'w') as file:
            file.write(json.dumps(latest_response, indent = 4))
            file.close()

    return changed_keys

if __name__ == "__main__":
    """
    Runs the do_compare function that compares the old response with the new and
    looking for changes. 
    Ret
    """
    compared = do_compare()
    if haschanged.has_changed(compared):
        do_log(compared)
        #TODO: => Add email, SMS, slack?
        pass
