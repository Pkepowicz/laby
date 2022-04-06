import time

loop = True
while loop:
    word = input("Podaj slowo: ")
    if word.find(' ') == -1:
        loop = False
    else:
        print("Nie podano slowa")
word = word.lower()
f = open('SJP.txt', 'r', encoding = 'utf-8')
loop = True
t1 = time.time()
for line in f:
    if word + '\n' == line:
        print(word, "znajduje sie w slowniku!")
        loop = False
    if loop == False:
        break
if loop == True:
    print(word, "nie znajduje sie w slowniku")
print("czas wykonywaniaa:", time.time() - t1, 's')