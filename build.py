import requests
import json
from imports import compare,haschanged, fetch_keys


if __name__ == "__main__":
    try:
        #Test with real request on example json.
        r = requests.get('https://jsonplaceholder.typicode.com/posts')
        #r = requests.get('https://gorest.co.in/public/v2/posts/100/comments')

        change = compare.do_compare(r.json())

        if haschanged.has_changed(change):
            """
#            ADD ALERT => Email, sms, slack ? 
            """
            print(change, "\n")
            with open("something.json", 'w') as file:
                file.write(json.dumps(r.json(), indent = 4))

    except:
        print("Something went wrong")



