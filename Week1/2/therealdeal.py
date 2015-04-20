import math


def sum_of_divisors(n):
    list_of_divisors = []
    number = 1
    while number <= n:
        if n % number == 0:
            list_of_divisors.append(number)
        number += 1
        sum_div = sum(list_of_divisors)
    return sum_div

print(sum_of_divisors(8))


def is_prime(n):
    if n in [0, 1]:
        return False
    elif n == 2:
        return True
    elif n < 0:
        return False
    else:
        for number in range(2, n):
            if (number != n) and (n % number == 0):
                return False
            else:
                return True

print(is_prime(-7))


def prime_number_of_divisors(n):
    if n in [0, 1]:
        return False
    elif n == 2:
        return True
    elif n < 0:
        return False
    else:
        for number in range(2, n):
            count_div = 0
            if (number != n) and (n % number == 0):
                count_div += 1
                return False
            else:
                return True

print(prime_number_of_divisors(7))


def contains_digit(number, digit):
    if str(digit) in str(number):
        return True
    else:
        return False

print(contains_digit(1233, 3))


def contains_digits(number, digits):
    string = str(number)
    for element in digits:
        if str(element) in string:
            continue
        else:
            return False
            break
    return True

print(contains_digits(402123, [0, 3, 4, 8]))


def count_substrings(haystack, needle):
    return haystack.count(needle)

print(count_substrings("This is a test string", "isi"))


def sum_matrix(m):
    sum = 0
    for i in m:
        for j in i:
            sum += j
    return sum

print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
