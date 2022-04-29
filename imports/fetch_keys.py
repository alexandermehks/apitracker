"""
Can be optimized very much, key.keys() generates a dict that can be returned directly.

Idea: instead of iterating over all the keys check the length of the dict (generated by key.keys()) to be able to
catch if a key has been added for a specific json object. 

len(key.keys()) => check for same length != iterate over the specific dict for new key
"""
def keys(data):
    key_holder = [] 
    for key in data:
        for k in key.keys():
            if k not in key_holder:
                key_holder.append(k)
    return key_holder
