# Сделайте игру крестики - нолики, человек должен играть с ботом, поле 3*3.
# Конечно, бот не должен ходить на занятые поля
# Если есть желание, то можете наделить бота псевдоинтеллектом,чтоб он ходил как можно ближе к своим занятым клеткам
# После каждого хода на экран должна выводиться текущая обстановка на поле.
from os import system

def printField():
    print(" ", ticTacToe[0][0], "|", ticTacToe[0][1], "|", ticTacToe[0][2], " ")
    print("-------------")
    print(" ", ticTacToe[1][0], "|", ticTacToe[1][1], "|", ticTacToe[1][2], " ")
    print("-------------")
    print(" ", ticTacToe[2][0], "|", ticTacToe[2][1], "|", ticTacToe[2][2], " ")

def gameprogress():
    global need_check, move_counter, game_win, game_over
    if need_check == False:
        if move_counter >= 5:
            need_check = True
    if need_check == True:
        game_win = check_win()
    if game_win:
        print("Есть победа!")
    if (move_counter == 9) and (not game_win):
        game_over = True
        print("Нет победителя")
    if (not game_win) and (not game_over):
        move_counter += 1
        moveInit()

def botMove(ba:int, bb:int):
    if check_win() == False:
        global move_counter
        tempndx = ba*10 + bb
        line_found = False
        field_found = False
        while not field_found:
            for i in range(8):
                for j in range(3):
                    if tempndx in wintemp[i]:
                        line_found = True
                if line_found:
                    for k in range(3):
                        if ticTacToe[wintemp[i][k]//10][wintemp[i][k]%10]==" ":
                            ticTacToe[wintemp[i][k]//10][wintemp[i][k]%10] = "O"
                            field_found = True
                            break
                if field_found:
                    break
        system("clear")
        move_counter += 1
        printField()
    gameprogress()

def enterData(a:int, b:int):
    ticTacToe[a-1][b-1] = "X"
    system("clear")
    printField()
    botMove(a-1, b-1)

def check_win():
    stringXO=""
    for i in range(8):
        for k in range(3):
            stringXO+=ticTacToe[wintemp[i][k]//10][wintemp[i][k]%10]
        if stringXO == "XXX" or stringXO == "OOO":
            #print(stringXO)
            return True
        else:
            stringXO = ""
    return False

def moveInit():
    posY = int(input("Задайте поле строка Y (от 1 до 3): "))
    posX = int(input("Задайте поле столбец X (от 1 до 3): "))
    enterData(posY, posX)

move_counter = 0
need_check = False
game_win = False
game_over = False
ticTacToe = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
wintemp=[[0, 1, 2], [10, 11, 12], [20, 21, 22], [0, 11, 22], [2, 11, 20], [0, 10, 20], [1, 11, 21], [2, 12, 22]]
printField()
gameprogress()