example_JSON = {
    "glossary": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": ["GML", "XML"]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    },
    

}

"""
The search takes an argument of an incoming response from the API you are using.
The old response gets stored locally to match against the new one for changes.

TODO:
 *Check for changes in keys or values. 
"""
def search(json_data):
    change_dict = {}
    change_dict["removed_keys"] = [] 
    change_dict["removed_values"] = []
    change_dict["added_keys"] = []
    change_dict["added_values"] = []

    #Latest response from API.
    latest_response_keys = json_data.keys()
    latest_response_values = json_data.values()

    #Stored API response.
    old_response_keys = example_JSON.keys()
    old_response_values = example_JSON.values()

    #If something has been removed from the response.
    if len(latest_response_keys) < len(old_response_keys):
        keys_removed = True
    else:
        keys_removed = False

    if len(latest_response_values) < len(old_response_values):
        values_removed = True
    else:
        values_removed = False
        asdad

    #Iterating over the latest response, looking at keys in the response.
    for key in latest_response_keys:
        if keys_removed:
            for old_key in old_response_keys:
                if old_key not in latest_response_keys:
                    change_dict["removed_keys"].append(old_key)
        else:
            if key not in old_response_keys:
                change_dict["added_keys"].append(key)

    #Iterating over the latest response, looking at the values in the response.
    for value in latest_response_values:
        if values_removed:
            if values_removed:
                for old_value in old_response_values:
                    if old_value not in latest_response_values:
                        change_dict["removed_values"].append(old_value)
        else:
            if value not in old_response_values:
                change_dict["added_values"].append(value)

    return change_dict
