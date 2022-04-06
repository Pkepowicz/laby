#modul
class LICZBA:
    def __init__(self, i):
        if type(i) == int:
            self.i = i
        else:
            raise TypeError("Podaj int")
    def DODAJ(self, other):
        if type(other) == LICZBA:
            return self.i + other.i
        elif type(other) == WYRAZ:
            return ord(other.s[-1]) + self.i
        else:
            raise NotImplementedError()
    def ODEJMIJ(self, other):
        if type(other) == LICZBA:
            return self.i - other.i
        elif type(other) == WYRAZ:
            return "???"
        else:
            raise NotImplementedError()

class WYRAZ:
    def __init__(self, wyraz):
        if type(wyraz) == str:
            self.s = wyraz
        else:
            raise TypeError("Podaj string")
    def DODAJ(self, other):
        if type(other) == WYRAZ:
            return self.s + other.s
        elif type(other) == LICZBA:
            return ord(self.s[-1]) + other.i
        else:
            raise NotImplementedError()
    def ODEJMIJ(self, other):
        if type(other) == LICZBA:
            return '???'
        elif type(other) == WYRAZ:
            if len(other.s) >= len(self.s):
                return other.s
            else:
                return self.s
        else:
            raise NotImplementedError()

i1 = LICZBA(2)
s1 = WYRAZ("abcdfg")
i2 = LICZBA(5)
s2 = WYRAZ("hijklmn")

print(i1.DODAJ(i2))
print(i1.DODAJ(s1))
print(s1.DODAJ(s2))
print(s1.DODAJ(i2))
print('-----------')
print(i1.ODEJMIJ(i2))
print(i1.ODEJMIJ(s1))
print(s1.ODEJMIJ(s2))
print(s1.ODEJMIJ(i2))