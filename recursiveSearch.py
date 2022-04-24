
s_JSON = {
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
    "hej": {
    	"svejs": "h"
    }

}

"""
The search takes an argument of an incoming response from the API you are using.
The old response gets stored locally to match against the new one for changes.

TODO:
 *Check for changes in keys or values. 
"""
def rec_search(json_data):
	change_dict = {}
	current_response_keys = json_data.keys()
	current_response_values = json_data.values()

	old_response_keys = s_JSON.keys()
	old_response_values = s_JSON.values()














