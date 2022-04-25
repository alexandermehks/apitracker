from imports import compare

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
         "Test": {
        "king": "kung"
    }
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

    key_compare = compare.key_compare(latest_response_keys,old_response_keys, keys_removed)
    change_dict = key_compare

    return change_dict
