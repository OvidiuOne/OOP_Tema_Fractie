import math as f
from fractions import Fraction

class Fraction:
    count = 0

    def __init__(self, numerator, denominator):
        gcd = f.gcd(numerator, denominator)
        self.num = int(numerator/gcd)
        self.den = int(denominator/gcd)

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den= self.den * other.den
        return Fraction(new_num, new_den)

    def inverse(self):
        return Fraction(self.den, self.num)

f1 = Fraction(1, 8)
f2 = Fraction(3, 4)
f3 = f1 + f2
f4 = f1 - f2
f5 = f1.inverse()

for f in [f1, f2, f3, f4, f5]:
    if isinstance(f, Fraction):
        print(f, "is a fraction")
    else:
        print(f, "is not a fraction")

######