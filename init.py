import requests
from imports import recursiveSearch

sample_JSON = {
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
                        "GlossSeeAlso": ["GML", "XML"],
                    },
                    "GlossSee": "markup"
                }
            }
        },
    },
    "Something": {
        "Color": "Red"
    }
}

if __name__ == "__main__":
    #Test with real request on example json.
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    change = recursiveSearch.search(r.json())
    print(change)


