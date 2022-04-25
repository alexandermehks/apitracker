#Can be optimized very much, key.keys() generates a dict that can be returned directly.
def keys(data):
    key_holder = [] 
    for key in data:
        for k in key.keys():
            if k not in key_holder:
                key_holder.append(k)
    return key_holder
