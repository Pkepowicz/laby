#generowanie listy
L = [1, 2]

for i in range(46):
    L.append((L[i] + L[i + 1]) / (L[i] - L[i + 1]))

print("Dlugość: ", len(L))
print(L)

#średnia
sr = 0
for f in L:
    sr += f

print("średnia: ", sr / len(L))

#moda
Md = {i:L.count(i) for i in L}
key = [k for k, v in Md.items() if v == max(Md.values())]
print("Wszystkie mody: ", key)

#te same wartosci
L.sort()
Re = []
for current, next in zip(L, L[1:]):
    if current == next:
        Re.append(current)
if(len(Re) == 0):
    print("Brak cyfr powtarzających się")
else:
    print(Re)