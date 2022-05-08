import sys
sys.path.append("../")
from logs.log import log_error,get_row,do_log
"""
If the return is not 0 it indicates and change in the response.

"""
def has_changed(data):
    try:
        changed = False
        for a in data["urls"]:
            if len(a["removed_keys"]) or len(a["added_keys"]) != 0:
                do_log(a)
                changed = True
        return changed

    except Exception as e:
        log_error(f"Something went wrong in {__file__} || {e}")	




