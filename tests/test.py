import unittest
import code

class TestCases(unittest.TestCase):

	def test_sanity(self):
		self.assertEqual(1, 1)


	'''
	Add your own test cases here
	function name must start with test_
	'''
	
	def test_noop(self):
		self.assertEqual(20, code.myFunc(10))

if __name__ == "__main__":
	unittest.main()
