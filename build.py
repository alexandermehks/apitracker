#!/usr/bin/env python3
import requests
import json
from imports import compare,haschanged, fetch_keys
from log import do_log

def run():
    try:
        #Test with real request on example json.
        r = requests.get('https://jsonplaceholder.typicode.com/posts')
        #r = requests.get('https://gorest.co.in/public/v2/posts/100/comments')

        change = compare.do_compare(r.json())

        if haschanged.has_changed(change):
            """
#            ADD ALERT => Email, sms, slack ? 
            """
            do_log(change)
            with open("latestResponse.json", 'w') as file:
                file.write(json.dumps(r.json(), indent = 4))
        else:
            print("No change in the response")
            do_log("No change in the response")

    except:
        print("Something went wrong")



if __name__ == "__main__":
   run() 


