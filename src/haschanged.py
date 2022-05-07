import sys
sys.path.append("../")
from logs.log import log_error,get_row
"""
If the return is not 0 it indicates and change in the response.

"""
def has_changed(data):
	try:
		if len(data["removed_keys"]) or len(data["added_keys"]) != 0:
			return True
		else:
			return False
	except Exception as e:
		log_error(f"Something went wrong in {__file__} || {e}")	




