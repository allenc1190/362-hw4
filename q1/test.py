import unittest
import main

class testCalc(unittest.TestCase):
	def test_positive(self):
		self.assertEqual(main.calcVol(2), 8)
		self.assertEqual(main.calcVol(3), 27)
		self.assertEqual(main.calcVol(4), 64)

	def test_negative(self):
		self.assertLessEqual(main.calcVol(-8), 0)
		self.assertLessEqual(main.calcVol(-6), 0)
		self.assertLessEqual(main.calcVol(-5), 0)

	def test_zero(self):
		self.assertLessEqual(main.calcVol(0), 0)

if __name__ == '__main__':
	unittest.main()