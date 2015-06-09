import unittest
from subprocess import check_output
from Node import *


class TestNF(unittest.TestCase):

	def test_topo1(self):
		ans = check_output(["python", "run_topo.py", "topo1", "topo1.log"])
		ans = ans.split('-----')[-2]
		ans = ''.join(ans.split('\n'))
		correct = __import__('topo1').ans
		self.assertEqual(ans, correct)

	def test_topo2(self):
		ans = check_output(["python", "run_topo.py", "topo2", "topo2.log"])
		ans = ans.split('-----')[-2]
		ans = ''.join(ans.split('\n'))
		correct = __import__('topo2').ans
		self.assertEqual(ans, correct)

	def test_topo3(self):
		ans = check_output(["python", "run_topo.py", "topo3", "topo3.log"])
		ans = ans.split('-----')[-2]
		ans = ''.join(ans.split('\n'))
		correct = __import__('topo3').ans
		self.assertEqual(ans, correct)

	def test_topo4(self):
		ans = check_output(["python", "run_topo.py", "topo4", "topo4.log"])
		ans = ans.split('-----')[-2]
		ans = ''.join(ans.split('\n'))
		correct = __import__('topo4').ans
		self.assertEqual(ans, correct)

	def test_topo5(self):
		ans = check_output(["python", "run_topo.py", "topo5", "topo5.log"])
		ans = ans.split('-----')[-2]
		ans = ''.join(ans.split('\n'))
		correct = __import__('topo5').ans
		self.assertEqual(ans, correct)

	def test_topo6(self):
		ans = check_output(["python", "run_topo.py", "topo6", "topo6.log"])
		ans = ans.split('-----')[-2]
		ans = ''.join(ans.split('\n'))
		correct = __import__('topo6').ans
		self.assertEqual(ans, correct)

	def test_topo7(self):
		ans = check_output(["python", "run_topo.py", "topo7", "topo7.log"])
		ans = ans.split('-----')[-2]
		ans = ''.join(ans.split('\n'))
		correct = __import__('topo7').ans
		self.assertEqual(ans, correct)

	def test_topo8(self):
		ans = check_output(["python", "run_topo.py", "topo8", "topo8.log"])
		ans = ans.split('-----')[-2]
		ans = ''.join(ans.split('\n'))
		correct = __import__('topo8').ans
		self.assertEqual(ans, correct)

	# TODO create more tests

if __name__ == '__main__':
	unittest.main()