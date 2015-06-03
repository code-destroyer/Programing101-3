import unittest
from thefinalround import *


class ThefinalroundTest(unittest.TestCase):

    def test_count_words(self):
        result = (count_words(["apple", "banana", "apple", "pie"]))
        self.assertEqual(result, {'apple': 2, 'banana': 1, 'pie': 1})

    def test_unique_words_count(self):
        result = (unique_words_count(["python", "python", "python", "ruby"]))
        self.assertEqual(result, 2)

    def test_nan_expand(self):
        result = (nan_expand(4))
        self.assertEqual(result, "\"Not a Not a Not a Not a NaN\"")

    def test_iterations_of_nan_expand(self):
        result = (iterations_of_nan_expand(
            'Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))
        result2 = (iterations_of_nan_expand("Show these people!"))
        self.assertEqual(result, 10)
        self.assertEqual(result2, False)

    def test_prime_factorization(self):
        result = (prime_factorization(356))
        self.assertEqual(result, [(2, 2), (89, 1)])

    def test_group(self):
        self.assertEqual(
            group([1, 1, 1, 2, 3, 1, 1]), [[1, 1, 1], [2], [3], [1, 1]])
        self.assertEqual(
            group([1, 2, 1, 2, 3, 3]), [[1], [2], [1], [2], [3, 3]])

    def test_cmax_consecutive(self):
        self.assertEqual(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]), 4)

    def test_groupby(self):
        self.assertEqual((groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7])),
                         {0: [0, 2, 4, 6], 1: [1, 3, 5, 7]})

    def test_prepare_meal(self):
        self.assertEqual(prepare_meal(7), '')
        self.assertEqual(prepare_meal(15), 'spam and eggs')
        self.assertEqual(prepare_meal(45), 'spam spam and eggs')

    def test_reduce_file_path(self):
        self.assertEqual(reduce_file_path("/"), '/')
        self.assertEqual(reduce_file_path("/srv/../"), '/')
        self.assertEqual(
            reduce_file_path("/srv/www/htdocs/wtf/"), '/srv/www/htdocs/wtf')
        self.assertEqual(
            reduce_file_path("/srv/www/htdocs/wtf"), '/srv/www/htdocs/wtf')
        self.assertEqual(reduce_file_path("/srv/./././././"), '/srv')
        self.assertEqual(reduce_file_path("/etc//wtf/"), '/etc/wtf')
        self.assertEqual(reduce_file_path("/etc/../etc/../etc/../"), '/')
        self.assertEqual(reduce_file_path("//////////////"), '/')
        self.assertEqual(reduce_file_path("/../"), '/')

    def test_is_an_ab(self):
        self.assertEqual(is_an_bn(""), True)
        self.assertEqual(is_an_bn("rado"), False)
        self.assertEqual(is_an_bn("aaabb"), False)
        self.assertEqual(is_an_bn("aaabbb"), True)
        self.assertEqual(is_an_bn("aabbaabb"), False)
        self.assertEqual(is_an_bn("bbbaaa"), False)
        self.assertEqual(is_an_bn("aaaaabbbbb"), True)

    def test_is_credit_card_valid(self):
        self.assertEqual(is_credit_card_valid(79927398713), True)
        self.assertEqual(is_credit_card_valid(79927398715), False)

    def test_goldbach(self):
        self.assertEqual(goldbach(10), [(3, 7), (5, 5)])

    def test_magic_square(self):
        self.assertEqual(
            magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), False)
        self.assertEqual(magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]), True)
        self.assertEqual(magic_square(
            [[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]), True)
        self.assertEqual(
            magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]), True)
        self.assertEqual(
            magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]), False)

    def test_friaday_years(self):
        self.assertEqual(friday_years(1000, 2000), 178)


if __name__ == '__main__':
    unittest.main()
