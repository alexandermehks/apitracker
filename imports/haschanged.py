"""
If the return is not 0 it indicates and change in the response.

"""
def has_changed(data):
	if len(data["removed_keys"]) or len(data["added_keys"]) != 0:
		return True
	else:
		return False
