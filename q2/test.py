import unittest
import main

class testList(unittest.TestCase):
	def test_avg(self):
		self.assertEqual(main.average([1, 2, 3]), 2)
		self.assertEqual(main.average([1, 1, 1]), 1)
	
	def test_len(self):
		self.assertEqual(main.retLen([1, 2, 3]), 3)
		self.assertEqual(main.retLen([]), 0)
		self.assertEqual(main.retLen([1,2,3,4]), 4)

	def test_n(self):
		self.assertEqual(main.retN(5), 5)
		self.assertEqual(main.retN(3), 3)
		self.assertEqual(main.retN(9), 9)

if __name__ == '__main__':
	unittest.main()