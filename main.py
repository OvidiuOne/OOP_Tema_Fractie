import math as np

class Fraction:
    count = 0

    def __init__(self, top, bottom):
        gcd = np.gcd(top, bottom)
        self.num = int(top/gcd)
        self.den = int(bottom/gcd)

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        new_top = self.num * other.den + self.den * other.num
        new_bottom = self.den * other.den
        return Fraction(new_top, new_bottom)

    def __sub__(self, other):
        top = self.num * other.den - self.den * other.num
        bottom = self.den * other.den
        return Fraction(top, bottom)

    def inverse(self):
        return Fraction(self.den, self.num)


f1 = Fraction(1, 8)
f2 = Fraction(3, 4)
print(f1)  # output: 1/2
print(f2)  # output: 3/4

f3 = f1 + f2
print(f3)  # output: 5/4

f4 = f1 - f2
print(f4)  # output: -1/4

f5 = f1.inverse()
print(f5)  # output: 2/1


######