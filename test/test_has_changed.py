import unittest
from sauronapeye.haschanged import has_changed

class TestHasChanged(unittest.TestCase):

	def test_has_changed_true(self):
		test_dict = {"removed_keys": ["Jane Doe"],
					 "added_keys": ["John Doe"]}
		self.assertTrue(has_changed(test_dict))

	def test_has_changed_false(self):
		test_dict = {"removed_keys": [],
					 "added_keys":[]}
		self.assertFalse(has_changed(test_dict))







if __name__ == "__main__":
	unittest.main()
