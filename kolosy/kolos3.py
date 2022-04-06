class CZYTELNIK:
    def OTWORZ(self, path):
        self.f = open(path, encoding='utf-8')
    def CZYTAM(self):
        parzysta = True
        linie = ''
        for i in self.f:
            if parzysta == True:
                parzysta = False
                continue
            else:
                linie += i
                parzysta = True
        return linie
    def SZUKAM(self, list, string):
        if list.find(string) == True:
            return True
        else:
            return False
    def LICZ(self, list, litera):
        return list.count(litera)
    def ZAMYKAM(self):
        self.f.close()


a = CZYTELNIK()
a.OTWORZ('przyslowia.txt')
L = []
L = a.CZYTAM()
print(L)
i = 97
wynik = []
while i <= 122:
    d = {'items':chr(i), 'values':a.LICZ(L, chr(i))}
    wynik.append(d)
    i += 1
key = sorted(wynik, key = lambda d: d['values'], reverse = True)
print('najwiecej razy wystapila litera',key[0]['items'], 'i wystapila', key[0]['values'], 'razy')
