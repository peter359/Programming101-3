def gcd(a, b):
    if a != 0:
        a = abs(a)
        b = abs(b)
        while a != b:
            if a < b:
                b -= a
            else:
                a -= b
    return b


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Cannot have 0 in denominator!")
        self.numerator = numerator // gcd(numerator, denominator)
        self.denominator = denominator // gcd(numerator, denominator)

    def __str__(self):
        if self.numerator % self.denominator == 0:
            return "{}".format(self.numerator)
        else:
            return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return Fraction(self.numerator * other. denominator + other.numerator * self.denominator, self.denominator * other.denominator)

    def __sub__(self, other):
        return Fraction(self.numerator * other. denominator - other.numerator * self.denominator, self.denominator * other.denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self. denominator == other. denominator
