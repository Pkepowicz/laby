tab = []
for i in range(500,3001):
    tab.append(i)
print(tab)
wynik = ""
for i in tab:
    if i % 7 == 0 and i % 5 != 0:
        wynik += str(i)
wynik = wynik.replace("21", "XX")
print(wynik)