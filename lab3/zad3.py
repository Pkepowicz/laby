import random
import math

#kolo
r = 3
a = r * (-1)
b = r
n = 1000

pin = 0
pout = 0
for i in range(n):
    x = random.uniform(a, b)
    y = random.uniform(a, b)
    if math.sqrt((x * x) + (y * y)) <= r:
        pin += 1
    else:
        pout += 1
print("Pole kola o promieniu", r, "wynosi", ((b - a) * (b - a)) * pin/(pin + pout))

#sinus
a = 2.0
b = 1.0
n = 1000
pin = 0
pout = 0
for i in range(n):
    x = random.uniform(0, a)
    y = random.uniform(0, b)
    if math.sin(x) >= y:
        pin += 1
    else:
        pout += 1
print("Pole sinusa w przedziale (0,2) wynosi", (a * b) * pin/(pin + pout))