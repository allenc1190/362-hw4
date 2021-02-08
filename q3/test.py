import unittest
import main

class testfirst(unittest.TestCase):
	def test_full(self):
		self.assertEqual(main.retFull('Allen', 'Chan'), 'Allen Chan')
		self.assertEqual(main.retFull('allen', 'chan'), 'allen chan')

	def test_first(self):
		self.assertEqual(main.fname('Allen'), 'Allen')
		self.assertEqual(main.fname('allen'), 'allen')

	def test_last(self):
		self.assertEqual(main.lname('Chan'), 'Chan')
		self.assertEqual(main.lname('chan'), 'chan')


if __name__ == '__main__':
	unittest.main()