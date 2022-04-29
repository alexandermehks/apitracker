from imports import compare,fetch_keys
import json
import os
import sys

PATH_JSON = sys.path[0] + "/something.json"

def key_compare(latest_response, old_response, removed):
    change_dict = {}
    change_dict["removed_keys"] = []
    change_dict["added_keys"] = []

    #Iterating over the latest response, looking at keys in the response.
    for key in latest_response:
        if removed:
            for old_key in old_response:
                if old_key not in latest_response and old_key not in change_dict["removed_keys"]:
                    change_dict["removed_keys"].append(old_key)
                    
        if key not in old_response:
            change_dict["added_keys"].append(key)
    return change_dict


"""
The search takes an argument of an incoming response from the API you are using.
The old response gets stored locally to match against the new one for changes.

 """
def do_compare(json_data):
    change_dict = {}
    change_dict["removed_keys"] = [] 
    change_dict["added_keys"] = []


    #Latest response from the API. Only looking at the keys. 
    latest_response_keys = fetch_keys.keys(json_data)

    #Stored API response.
    with open(PATH_JSON, "r") as file:
        data = json.loads(file.read())
        old_response_keys = fetch_keys.keys(data)
        file.close()

    #old_response_keys = example_JSON.keys() 
    #old_response_values = example_JSON.values()

    #If something has been removed from the response.
    if len(latest_response_keys) != len(old_response_keys):
        keys_removed = True
    else:
        keys_removed = False

    #if len(latest_response_values) < len(old_response_values):
    #    values_removed = True
    #else:
    #    values_removed = False
    key_compare = compare.key_compare(latest_response_keys,old_response_keys, keys_removed)
    change_dict = key_compare

    return change_dict
