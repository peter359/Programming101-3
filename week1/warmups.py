def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    first = 1
    second = 1
    if n == 1:
        return [first]
    a = [first, second]
    for i in range(1, n - 1):
        second += first
        first = second - first
        a += [second]
    return a


def sum_of_digits(n):
    n = abs(n)
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s


def fact_digits(n):
    s = 0
    while n > 0:
        s += factorial(n % 10)
        n = n // 10
    return s


def palindrome(obj):
    return str(obj) == str(obj)[::-1]


def to_digits(n):
    a = []
    while n != 0:
        a += [n % 10]
        n = n // 10
    return a[::-1]


def to_number(digits):
    n = 0
    power = len(digits) - 1
    for x in digits:
        n += x * 10 ** power
        power -= 1
    return n


def fib_number(n):
    a = fibonacci(n)
    b = ""
    for x in a:
        b += str(x)
    return int(b)


def count_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    c = 0
    for x in str:
        if x in vowels:
            c += 1
    return c


def count_consonants(str):
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
    c = 0
    for x in str:
        if x in consonants:
            c += 1
    return c


def char_histogram(string):
    h = {}
    for x in string:
        h[x] = string.count(x)
    return h


def p_score(n):
    if palindrome(n):
        return 1
    return 1 + p_score(n + int(str(n)[::-1]))


def is_increasing(seq):
    for a in range(len(seq) - 1):
        b = a + 1
        if seq[a] >= seq[b]:
            return False
    return True


def is_decreasing(seq):
    for a in range(len(seq) - 1):
        b = a + 1
        if seq[a] <= seq[b]:
            return False
    return True


def is_hack(n):
    b = bin(n)[2:]
    ones = b.count('1')
    return palindrome(b) and ones % 2 == 1


def next_hack(n):
    if is_hack(n):
        n += 1
    while not is_hack(n):
        n += 1
    return n
