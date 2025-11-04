import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import calculator

class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(calculator.fun1(2, 3), 5)
        self.assertEqual(calculator.fun1(-1, -1), -2)

    def test_fun2(self):
        self.assertEqual(calculator.fun2(3, 2), 1)
        self.assertEqual(calculator.fun2(-2, -3), 1)

    def test_fun3(self):
        self.assertEqual(calculator.fun3(2, 3), 6)
        self.assertEqual(calculator.fun3(-2, -3), 6)

    def test_fun4(self):
        self.assertEqual(calculator.fun4(1, 2, 3), 6)
        self.assertEqual(calculator.fun4(-1, -1, -1), -3)

if __name__ == '__main__':
    unittest.main()
