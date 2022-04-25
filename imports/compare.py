def key_compare(latest_response, old_response, removed):
    change_dict = {}
    change_dict["removed_keys"] = []
    change_dict["added_keys"] = []

    #Iterating over the latest response, looking at keys in the response.
    for key in latest_response:
        if removed:
            for old_key in old_response:
                if old_key not in latest_response:
                    change_dict["removed_keys"].append(old_key)
        else:
            if key not in old_response:
                change_dict["added_keys"].append(key)
    return change_dict
