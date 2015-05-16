from copy import deepcopy
from pprint import pprint


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


def to_digits(n):
    list_digits = []
    str_number = str(n)
    for element in range(0, len(str_number)):
        list_digits.append(int(str(n)[element]))
    return list_digits


def to_number(digits):
    number = ''
    for i in range(0, len(digits)):
        number = number + str(digits[i])
    return int(number)


def is_number_balanced(n):
    numbers = to_digits(n)
    numbers_reversed = numbers[::-1]
    length = len(numbers)
    sum_left = 0
    sum_right = 0
    for i in range(0, length // 2):
        sum_left += int(numbers[i])
    for element in range (0, len(numbers_reversed) // 2):
        sum_right += int(numbers_reversed[element])
    return sum_left == sum_right

print(is_number_balanced(1235421))


def count_substrings(haystack, needle):
    return haystack.count(needle)

print(count_substrings("This is a test string", "isi"))


def zero_insert(n):
    list_from_n = to_digits(n)
    print(list_from_n)
    r = []
    for x in range(0, len(list_from_n) - 1):
        r.append(list_from_n[x])
        if list_from_n[x] == list_from_n[x + 1] or (list_from_n[x] + list_from_n[x + 1]) % 10 == 0:
            r.append(0)
    r.append(list_from_n[-1])
    print (r)

    return to_number(r)

print(zero_insert(1164573))


def sum_matrix(matrix):
    sum = 0
    for element in matrix:
        for sub_element in element:
            sum += sub_element
    return sum

print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def bombed_matrix(m, i, j):
    indexes = [-1, 0, 1]
    bomb = deepcopy(m)
    for row in indexes:
        for col in indexes:
            if i + row >= 0:
                if i + row <= len(bomb) - 1:
                    if j + col >= 0:
                        if j + col <= len(bomb[0]) - 1:
                            if not(i + row == i and j + col == j):
                                if bomb[i][j] <= bomb[i + row][j + col]:
                                    bomb[i + row][j + col] -= bomb[i][j]
                                elif bomb[i][j] > bomb[i + row][j + col]:
                                    bomb[i + row][j + col] = 0
    return bomb


def matrix_bombing_plan(m):
    dictionary = {}

    for i in range(len(m)):
        for j in range(len(m[0])):
            total_sum = sum_matrix(bombed_matrix(m, i, j))
            dictionary[(i, j)] = total_sum

    return dictionary

pprint(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
