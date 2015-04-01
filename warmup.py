import math


def factorial(n):
    return math.factorial(n)

print (factorial(5))


def fibonachi(n):
    result = []
    for i in range(0, n):
        if i < 2:
            result.append(1)
        else:
            result.append(result[i - 1] + result[i - 2])
    return result

print(fibonachi(3))


def sum_of_digits(n):
    res = 0
    while n > 0:
        res += int(n % 10)
        n /= 10
    return res

"""def my_sum(n):
    res = []
    while n > 0 :
        res.append(n%10)
        n/=10
    return sum(res)"""

print(sum_of_digits(1325))


def fact_digits(n):
    list_dig = []
    for i in str(n):
        list_dig.append(int(i))
    sum_of_f_digits = 0
    for i in list_dig:
        sum_of_f_digits += math.factorial(i)
    return sum_of_f_digits

print(fact_digits(13))


def palindrome(obj):
    ls = []
    if type(obj) == str:
        for i in range(0, len(obj)):
            ls.append(obj[i])
    elif type(obj) == int:
        while obj > 0:
            ls.append(int(obj % 10))
            obj /= 10
    else:
        print ("Error!")
        return False
    length = len(ls)
    for i in range(0, length // 2):
        if ls[i] != ls[length - i - 1]:
            return False
    return True

print(palindrome(""))


def to_digits(n):
    list_digits = []
    string1 = str(n)
    for i in range(0, len(string1)):
        list_digits.append(int(i))
    return list_digits

print(to_digits(1234556))


def to_number(digits):
    number = ''
    for i in range(0, len(digits) + 1):
        number = number + str(i)
    return int(number)

print(to_number([1, 2, 3, 4]))


def fib_number(n):
    result = []
    for i in range(0, n):
        if i < 2:
            result.append(1)
        else:
            result.append(result[i - 1] + result[i - 2])
    number = ''
    for i in result:
        number = number + str(i)
    return int(number)

print(fib_number(12))


def count_vowels(str):
    counter = 0
    for i in str:
        if i in 'aioeuyAIOEUY':
            counter += 1
    return counter

print(count_vowels('Pythonyyyy'))


def count_consonants(str):
    counter_cons = 0
    str.lower()
    for i in str:
        if i in 'bcdfghjklmnpqrstvwxz':
            counter_cons += 1
    return counter_cons

print(count_consonants('aksjhalkgf'))


def char_histogram(string):
    dict_histogram = {}
    i = 0
    for char in string:
        if char in dict_histogram:
            dict_histogram[char] += 1
        else:
            dict_histogram[char] = 1
    return dict_histogram

print(char_histogram("Python!"))


def p_score(n):
    if palindrome(str(n)):
        return 1
    s = n + int(str(n)[::-1])
    return 1 + p_score(s)

print(p_score(484))


def is_increasing(seq):
    for element in range(0, len(seq) - 1):
        if seq[element] > seq[element + 1]:
            return False
    return True

print(is_increasing([1,2,3,4,5, -1]))


def is_decreasing(seq):
    for element in range(0, len(seq) - 1):
        if seq[element] < seq[element + 1]:
            return False
    return True

print(is_decreasing([5,4,3,2,1]))


def even(n):
    return n % 2 == 0


def odd(n):
    return not even(n)


def hack_number(n):
    if palindrome(bin(n)[2:]) and odd(bin(n)[2:].count("1")):
        return True
    return False

print(hack_number(6))


def next_hack(n):
    n += 1
    while not hack_number(n):
        n += 1
    return n

print(next_hack(10))
