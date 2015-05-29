from copy import deepcopy
from warmups import to_number, to_digits


def sum_of_divisors(n):
    s = 0
    for x in range(1, n + 1):
        if n % x == 0:
            s += x
    return s


def is_prime(n):
    n = abs(n)
    if n in [0, 1]:
        return False
    if n == 2:
        return True
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


def prime_number_of_divisors(n):
    c = 0
    for x in range(1, n + 1):
        if n % x == 0:
            c += 1
    return is_prime(c)


def contains_digit(number, digit):
    while number != 0:
        if digit == number % 10:
            return True
        number //= 10
    return False


def contains_digits(number, digits):
    a = to_digits(number)
    for x in digits:
        if x not in a:
            return False
    return True


def is_number_balanced(n):
    if n / 10 < 1:
        return True
    l = len(str(n))
    i = 0
    s1 = 0
    s2 = 0
    a = to_digits(n)
    while i < l // 2:
        s1 += a[i]
        i += 1
    i = l - 1
    while i >= l - l // 2:
        s2 += a[i]
        i -= 1
    return s1 == s2


def count_substrings(haystack, needle):
    br = 0
    i = 0
    while i < len(haystack):
        if needle == haystack[i:len(needle) + i]:
            br += 1
            i += len(needle) - 1
        i += 1
    return br


def zero_insert(n):
    a = to_digits(n)
    i = 0
    while i < len(a) - 1:
        if a[i] == a[i + 1] or (a[i] + a[i + 1]) % 10 == 0:
            a.insert(i + 1, 0)
            i += 1
        i += 1
    return to_number(a)


def sum_matrix(m):
    return sum([col for row in m for col in row])


def matrix_bombing_plan(m):
    a = {}
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            p = []
            for k in [-1, 1]:
                for l in [-1, 1]:
                    n = deepcopy(m)
                    if i + k >= 0 and i + k < len(n) and j + l >= 0 and j + l < len(n[i]):
                        n[i + k][j] = max(0, n[i + k][j] - n[i][j])
                        n[i][j + l] = max(0, n[i][j + l] - n[i][j])
                        n[i + k][j + l] = max(0, n[i + k][j + l] - n[i][j])
                    p += [n]
            q = deepcopy(m)
            for g in range(0, len(q)):
                for h in range(0, len(q[g])):
                    q[g][h] = min(p[0][g][h], p[1][g][h], p[2][g][h], p[3][g][h])
            a[(i, j)] = sum_matrix(q)
    return a
