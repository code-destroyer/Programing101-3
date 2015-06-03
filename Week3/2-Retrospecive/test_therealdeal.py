import unittest
from therealdeal import *


class TherealdealTest(unittest.TestCase):

    def test_sum_of_divisors(self):
        result = (sum_of_divisors(8))
        self.assertEqual(result, 15)

    def test_is_prime(self):
        result = (is_prime(-7))
        self.assertEqual(result, False)

    def test_prime_number_of_divisors(self):
        result = (prime_number_of_divisors(7))
        self.assertEqual(result, True)

    def test_contains_digit(self):
        result = (contains_digit(1233, 3))
        self.assertEqual(result, True)

    def test_contains_digits(self):
        result = (contains_digits(402123, [0, 3, 4, 8]))
        self.assertEqual(result, False)

    def test_is_number_balances(self):
        result = (is_number_balanced(1235421))
        self.assertEqual(result, False)

    def test_count_substrings(self):
        result = (count_substrings("This is a test string", "isi"))
        self.assertEqual(result, 0)

    def test_zero_insert(self):
        result = (zero_insert(1164573))
        self.assertEqual(result, 1016045703)

    def test_sum_matrix(self):
        result = (sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        self.assertEqual(result, 45)

    def test_matrix_bombing_plan(self):
        result = (matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        self.assertEqual(result, {(0, 0): 42,
                                     (0, 1): 36,
                                     (0, 2): 37,
                                     (1, 0): 30,
                                     (1, 1): 15,
                                     (1, 2): 23,
                                     (2, 0): 29,
                                     (2, 1): 15,
                                     (2, 2): 26})


if __name__ == '__main__':
    unittest.main()
