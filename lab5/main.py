from math import pow
from collections import deque

TOWER_SIZE = 6

###########################################################
#           PODEJSCIE REKURENCYJNE
def hanoi_Rec(n, sour, dest, buff, moves) -> None:
    if n == 1:
        moves.append('Z ' + sour + " przeniesiono na " + dest)
    else:
        hanoi_Rec(n - 1, sour, buff, dest, moves)
        moves.append('Z ' + sour + " przeniesiono na " + dest)
        hanoi_Rec(n - 1, buff, dest, sour, moves)

file = open('odpowiedzi_rek.txt', 'w')
moves = []
source = '1'
destination = '2'
buffer = '3'

hanoi_Rec(TOWER_SIZE, source, destination, buffer, moves)
for i in moves:
    file.write(i + '\n')
file.write('Wystarczylo: ' + str(len(moves)) + ' ruchow')
file.close()

############################################################
#           PODEJSCIE ITERACYJNE
def hanoi_Iter(n, sour:list, dest:list, buff:list, moves) -> None:
    if n % 2 == 0: #zamiana wiezy docelowej
        dt = '3'
        bf = '2'
    else:
        dt = '2'
        bf = '3'
    for i in range(1, int(pow(2, n))):
        if i%3 == 1:
            if len(dest) == 0:
                dest.insert(0, sour.pop(0))
                moves.append("Z 1 przeniesiono na " + dt)
            elif len(sour) == 0:
                sour.insert(0, dest.pop(0))
                moves.append("Z " + dt + " przeniesiono na 1")
            elif sour[0] < dest[0]:
                dest.insert(0, sour.pop(0))
                moves.append("Z 1 przeniesiono na " + dt)
            elif dest[0] < sour[0]:
                sour.insert(0, dest.pop(0))
                moves.append("Z " + dt + " przeniesiono na 1")
        if i%3 == 2:
            if len(buff) == 0:
                buff.insert(0, sour.pop(0))
                moves.append("Z 1 przeniesiono na " + bf)
            elif len(sour) == 0:
                sour.insert(0, buff.pop(0))
                moves.append("Z " + bf + " przeniesiono na 1")
            elif buff[0] < sour[0]:
                sour.insert(0, buff.pop(0))
                moves.append("Z " + bf + " przeniesiono na 1")
            elif sour[0] < buff[0]:
                buff.insert(0, sour.pop(0))
                moves.append("Z 1 przeniesiono na " + bf)
        if i%3 == 0:
            if len(dest) == 0:
                dest.insert(0, buff.pop(0))
                moves.append("Z " + bf + " przeniesiono na " + dt)
            elif len(buff) == 0:
                buff.insert(0, dest.pop(0))
                moves.append("Z " + dt + " przeniesiono na " + bf)
            elif buff[0] < dest[0]:
                dest.insert(0, buff.pop(0))
                moves.append("Z " + bf + " przeniesiono na " + dt)
            elif dest[0] < buff[0]:
                buff.insert(0, dest.pop(0))
                moves.append("Z " + dt + " przeniesiono na " + bf)
        i += 1

file = open('odpowiedzi_iter.txt', 'w')
source = [i for i in range(1, TOWER_SIZE + 1)]
destination = []
buffer = []
moves = []

hanoi_Iter(TOWER_SIZE, source, destination, buffer, moves)
for i in moves:
    file.write(i + '\n')
file.write('Wystarczylo: ' + str(len(moves)) + ' ruchow')
file.close()

###########################################################
#           CZAS WYKONYWANIA
