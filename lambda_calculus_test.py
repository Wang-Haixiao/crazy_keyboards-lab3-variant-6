import unittest

from lambda_calculus import *


class TestLambdaCalculus(unittest.TestCase):
    def test_and(self):
        """True & True = True, True & False = False, False & False = False"""
        self.assertEqual(str(calculus(func_and(TRUE, TRUE))), str(TRUE))
        self.assertEqual(str(calculus(func_and(TRUE, FALSE))), str(FALSE))
        self.assertEqual(str(calculus(func_and(FALSE, FALSE))), str(FALSE))

    def test_or(self):
        """True or True = True, True or False = True, False or False = False"""
        self.assertEqual(str(calculus(func_or(TRUE, TRUE))), str(TRUE))
        self.assertEqual(str(calculus(func_or(TRUE, FALSE))), str(TRUE))
        self.assertEqual(str(calculus(func_or(FALSE, FALSE))), str(FALSE))

    def test_not(self):
        """not True = False, not False = True"""
        self.assertEqual(str(calculus(func_not(TRUE))), str(FALSE))
        self.assertEqual(str(calculus(func_not(FALSE))), str(TRUE))

    def test_succ(self):
        """2 + 1 = 3"""
        arr1 = str(calculus(func_succ(func_numbers(2))))
        arr2 = str(func_numbers(3))
        self.assertEqual(arr1, arr2)

    def test_pred(self):
        """2 - 1  = 1"""
        arr1 = str(calculus(func_pred(func_numbers(2))))
        arr2 = str(func_numbers(1))
        self.assertEqual(arr1, arr2)

    def test_plus(self):
        """2 + 3 = 5"""
        arr1 = str(calculus(func_plus(func_numbers(2), func_numbers(3))))
        arr2 = str(func_numbers(5))
        self.assertEqual(arr1, arr2)

    def test_multiply(self):
        """2 * 3 = 6"""
        arr1 = str(calculus(func_multiply(func_numbers(2), func_numbers(3))))
        arr2 = str(func_numbers(6))
        self.assertEqual(arr1, arr2)


if __name__ == '__main__':
    unittest.main()
