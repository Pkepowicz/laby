import random

def plansza(state):
    print("------------- \n|", state[0],"|", state[1], "|", state[2], "| \n-------------\n|", state[3],"|", state[4], "|", state[5], "| \n-------------\n|", state[6],"|", state[7], "|", state[8], "| \n-------------")

def ruch(int):
    print(int)

def wynik(int, state, player):
    #pionowo
    column = int % 3
    if state[column] == player and state[column + 3] == player and state[column + 6] == player:
        print("Wygral: ", player)
        return False
    #poziomo
    row = 0
    if int >= 0 and int <= 2:
        row = 0
    if int >= 3 and int <= 5:
        row = 3
    if int >= 6 and int <= 8:
        row = 6
    if state[row] == player and state[row + 1] == player and state[row + 2] == player:
        print("Wygral: ", player)
        return False
    #skos
    if state[0] == player and state[4] == player and state[8] == player:
        print("Wygral: ", player)
        return False
    if state[2] == player and state[4] == player and state[6] == player:
        print("Wygral: ", player)
        return False

state = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
plansza(state)
IsPlayerTurn = True
IsGameOn = True
while True:
    while IsPlayerTurn:
        a = input("Gdzie postawić o?: ")
        if a == 'q':
            IsGameOn = False
            break
        try:
            a = int(a) - 1
            if a < 0:
                print("Blad przy wprowadzaniu pozycji")
                continue
            if state[int(a)] != ' ':
                print("Pozycja zajeta")
            else:
                state[int(a)] = 'o'
                IsGameOn = wynik(int(a), state, 'o')
                IsPlayerTurn = False
        except:
            print("Blad przy wprowadzaniu pozycji")
            continue
    if IsGameOn == False:
        plansza(state)
        break
    while not IsPlayerTurn:
        bot = random.randint(0,8)
        if state[bot] == ' ':
            state[bot] = 'x'
            IsGameOn = wynik(bot, state, 'x')
            IsPlayerTurn = True
    if IsGameOn == False:
        plansza(state)
        break
    plansza(state)