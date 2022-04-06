import math
import sys


class circle:
    r = 0
    def __init__(self, R):
        if R <= 0:
            print("blad")
            sys.exit()
        else:
            self.r = R
    def area(self):
        return math.pi * self.r * self.r
    def circ(self):
        return 2 * math.pi * self.r

class square:
    a = 0
    def __init__(self, A):
        if A <= 0:
            print('blad')
            sys.exit()
        else:
            self.a = A
    def area(self):
        return self.a * self.a
    def circ(self):
        return 4 * self.a

class triangle:
    a = 0
    b = 0
    c = 0
    def __init__(self, A, B, C):
        list = [A, B, C]
        list.sort()
        if list[0] + list[1] <= list[2]:
            print("blad")
            sys.exit()
        else:
            self.a = list[0]
            self.b = list[1]
            self.c = list[2]
    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    def circ(self):
        return self.a + self.b + self.c