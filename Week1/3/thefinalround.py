import math


def count_words(arr):
    result = {}
    for word in arr:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

print(count_words(["apple", "banana", "apple", "pie"]))


def unique_words_count(arr):
    return len(set(arr))
    # result = {}
    # for word in arr:
    #     if word in result:
    #         result[word] += 1
    #     else:
    #         result[word] = 1
    # return len(result)

print(unique_words_count(["python", "python", "python", "ruby"]))


def nan_expand(times):
    result = 0
    if times == 0:
        return "\"\""
    else:
        for time in range(0, times):
            result += 1
        list_r = []
        for element in range(0, result):
            list_r.append(element)
        str_r = '\"'
        for n in list_r:
            str_r += ("Not a ")
        str_r += ("NaN\"")
    return str_r

print(nan_expand(4))


def iterations_of_nan_expand(expanded):
    string = 'Not a'
    if expanded.count(string) == 0:
        return False
    else:
        return expanded.count(string)

print(iterations_of_nan_expand(
    'Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))
print(iterations_of_nan_expand("Show these people!"))


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


def prime_factorization(n):
    primes = []
    for i in range(0, n):
        if is_prime(i) == True:
            if n % i == 0:
                n = n // i
                primes.append(i)
                if n % i == 0:
                    n = n // i
                    primes.append(i)
    result = {}
    for prime in primes:
        if prime in result:
            result[prime] += 1
        else:
            result[prime] = 1
    return sorted(result.items())

print(prime_factorization(356))


def group(list_int):
    big_tuple = []
    small_tuple = []
    for element in range(0, len(list_int)):
        if list_int[element] in small_tuple or small_tuple == []:
            small_tuple.append(list_int[element])
        else:
            big_tuple.append(small_tuple)
            small_tuple = []
            small_tuple.append(list_int[element])
    big_tuple.append(small_tuple)
    return big_tuple

print(group([1, 1, 1, 2, 3, 1, 1]))


def goldbach(n):
    list_gold = []
    list_final = []
    for element in range(0, n//2+1):
            if is_prime(element) and is_prime(n - element) == True:
                list_final.append((element, n-element))
    return list_final

print(goldbach(10))


def max_consecutive(items):
    counter = 0
    group_list = group(items)
    for element in group_list:
        if counter < len(element):
            counter = len(element)
        elif counter >= len(element):
            continue
    return counter

print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
