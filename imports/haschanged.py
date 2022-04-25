def has_changed(data):
	if len(data["removed_keys"]) or len(data["added_keys"]) != 0:
		return True
	else:
		return False
