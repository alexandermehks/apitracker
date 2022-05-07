from helpers import fetch_keys
import json
import os
import sys
import sys
sys.path.append("../")
from logs.log import log_error,get_row

def key_compare(latest_response: list, old_response: list):
    try:
        change_dict = {}
        change_dict["removed_keys"] = []
        change_dict["added_keys"] = []

        #If the length of the new and old response are not the same.
        if len(latest_response) != len(old_response):
            modified = True
        else:
            modified = False

        #Iterating over the latest response, looking at keys in the response.
        for key in latest_response:
            if modified:
                for old_key in old_response:
                    if old_key not in latest_response and old_key not in change_dict["removed_keys"]:
                        change_dict["removed_keys"].append(old_key)

            if key not in old_response:
                change_dict["added_keys"].append(key)
        return change_dict

    except Exception as e:

        log_error(f"Something went wrong in {__file__} || {e} ")  




