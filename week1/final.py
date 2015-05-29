from deal import is_prime


def count_words(arr):
    result = {}
    for word in arr:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result


def unique_words_count(arr):
    return len(count_words(arr))


def nan_expand(times):
    NaN = ""
    if times >= 1:
        NaN = "Not a NaN"
    for i in range(1, times):
        NaN = "Not a " + NaN
    return NaN


def iterations_of_nan_expand(expanded):
    if len(expanded) == 0:
        return 0
    if len(expanded) == 9:
        if expanded == nan_expand(1):
            return 1
        else:
            return False
    if expanded == nan_expand((len(expanded) - 3) // 6):
        return (len(expanded) - 3) // 6
    return False


def get_prime_divisors(n):
    return [x for x in range(1, n + 1) if n % x == 0 and is_prime(x)]


def is_prime(n):
    if n in [0, 1]:
        return False
    if n == 2:
        return True
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


def prime_factorization(n):
    result = []
    for divisor in get_prime_divisors(n):
        count = 0
        while n % divisor == 0:
            count += 1
            n //= divisor
        result.append((divisor, count))
    return result


def group(items):
    arr = []
    i = 0
    while i < len(items) - 1:
        temp = [items[i]]
        while i < len(items) - 1 and items[i] == items[i + 1]:
            temp.append(items[i + 1])
            i += 1
        arr.append(temp)
        i += 1
    if i < len(items) and items[i - 1] != items[i]:
        arr.append([items[i]])
    return arr


def max_consecutive(items):
    return max([len(g) for g in group(items)])


def groupby(func, seq):
    result = {}
    for i in seq:
        if func(i) in result:
            result[func(i)].append(i)
        else:
            result[func(i)] = [i]
    return result


def prepare_meal(number):
    if number == 5:
        return "eggs"
    meal = ""
    if number % 5 == 0 and number != 0:
        meal += "and eggs"
        number //= 5
    n = 0
    while number % 3 == 0:
        number //= 3
        n += 1
    if number == 1:
        meal = n * "spam " + meal
    if "and" not in meal:
        meal = meal[:len(meal) - 1]
    return meal


def is_an_bn(word):
    l = len(word) // 2
    return word[:l] == "a" * l and word[l:] == "b" * l


def is_credit_card_valid(number):
    arr = [int(n) for n in str(number)][::-1]
    odd = [arr[i] * 2 for i in range(0, len(arr)) if i % 2 == 1]
    odd = [sum([int(p) for p in str(n)]) for n in odd]
    even = [arr[i] for i in range(0, len(arr)) if i % 2 == 0]
    return sum(odd + even) % 10 == 0 and len(arr) % 2 == 1


def goldbach(n):
    r = range(2, n // 2 + 1)
    return [(i, n - i) for i in r if is_prime(i) and is_prime(n - i)]


def magic_square(matrix):
    l = len(matrix)
    r = range(0, l)
    rows = []
    for i in r:
        rows.append(sum(matrix[i]))
    cols = []
    for j in r:
        s = 0
        for i in r:
            s += matrix[i][j]
        cols.append(s)
    m_diagonal = sum([matrix[i][j] for i in r for j in r if i == j])
    bm_diagonal = sum([matrix[i][j] for i in r for j in r if i + j == l - 1])
    rows.append(m_diagonal)
    cols.append(bm_diagonal)
    for n in range(0, len(rows) - 1):
        if rows[n] != rows[n + 1] or cols[n] != cols[n + 1]:
            return False
    return rows[0] == cols[0]
