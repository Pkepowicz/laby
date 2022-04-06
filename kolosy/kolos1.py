import random
from statistics import median
class lista:
    l = []
    def __init__(self):
        for i in range(500):
            self.l.append(random.randint(0,100))
    def ph(self):
        print(self.l)
    def najmniejsza(self):
        self.l.sort()
        return self.l[0]
    def najwieksza(self):
        self.l.sort()
        return self.l[-1]
    def moda(self):
        Md = {i:self.l.count(i) for i in self.l}
        key = [k for k, v in Md.items() if v == max(Md.values())]
        return key
    def mediana(self):
        return median(self.l)

a = lista()
print(a.najmniejsza())
print(a.najwieksza())
print(a.moda())
print(a.mediana())
a.ph()
f = open('wyniki.txt', 'w')
f.write(str(a.najmniejsza()) + '\n')
f.write(str(a.najwieksza()) + '\n')
f.write(str(a.moda()) + '\n')
f.write(str(a.mediana()) + '\n')
f.close()