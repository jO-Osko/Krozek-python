# Dva načina
# Lahko vemo x in y ali pa kot in dolžino

import math

c ** (a/b)

class Kompleksno:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # return f"{self.x} + {self.y}i"
        return str(self.x) + " + " + str(self.y) + "i"

    # self + other
    def __add__(self, other):
        return Kompleksno(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Kompleksno(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)

    def __abs__(self):
        return (self.x * self.x + self.y * self.y)**0.5

    # self / other
    def __truediv__(self, other):
        ab = abs(other)**2
        return self * Kompleksno(other.x/ab, -other.y/ab)

    def kot(self):
        if self.x == 0 and self.y == 0:
            return 0
        return math.degrees(math.atan2(self.y, self.x))

def sestej_stevili(a, b):
    return Kompleksno(a.x + b.x, a.y + b.y)

def zmnozi(a, b):
    # (x1 + y1i) * (x2 + y2i) = (x1*x2 - y1*y2) + (x1*y2 + x2*y1)*i
    return Kompleksno(a.x * b.x - a.y * b.y, a.x * b.y + a.y * b.x)

a = Kompleksno(3, 4) # 3 + 4i
b = Kompleksno(0, 1) # 0 + 1i

print("Kot števila a je:", a.kot(), " stopinj")
c = a * b
print(abs(a), abs(b), abs(a) * abs(b), abs(c))
print(c / b, a)
print(a / b, (a/b) * b)
print(a/a, b/b)
print(a)
print(b)
print(a + b)
print(a * b)
