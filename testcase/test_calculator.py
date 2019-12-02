import unittest
from testcase.calculator import add, subtract


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_substract(self):
        self.assertRaises(ValueError, subtract(10, 0))


if __name__ == '__main__':
    unittest.main()