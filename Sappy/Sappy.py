from random import shuffle
from tkinter import Tk
from tkinter import Canvas
from os import system
answer = 'Y'
time = 0
looses_in_row = 0
while answer in ['Y','y']:
    if time == 0:
        print("\n  Game \"Sappy\".")
        print("\n  Version 1.2.0, Date 20.05.2017.")
        print("\n  Deverlopers: Bryzgalov Fedor, Putimcev Yury.")
    print("\n  In order to win, you need to guess by checking all the places where there are no bombs.")
    print("  If successful, you will be guessing the cell shows the number of bombs around this cell.")
    print("\n  After entering the field dimension should open a window where you can see the information:")
    print("  1) Blue color will mark open cells you;\n  2) The yellow color will marked bomb exploded you;")
    print("  3) Green color will mark the cells that you have not opened;\n  4) The red cells will be marked, in which a bomb.")
    if time == 0:
        N = int(input('\n  Enter the size of the field (number).\n> '))
        while True:
            if N > 7:
                N = int(input("  The program supports a maximum field of 7x7, enter the number <= 7.\n> "))
            elif N < 2:
                N = int(input("  The program supports the field at least 2x2, enter the number >= 2.\n> "))
            else:
                break
        if N >= 2 and N < 4:
            print("  Note! For normal operation of the program is better to choose 4x4 box above.")
    print("\n  You have chosen the size of the field ", N, "x", N, sep = "", end = ".\n")
    if looses_in_row > 2 and difficulty != 1:
        wait = input('\n  You lose a few times in a row! We recommend you to change the difficulty.')
    difficulty = int(input("\n  Select the difficulty (number):\n  1) Easy;\n  2) Medium;\n  3) Hard;\n  4) Expert.\n> "))
    while True:
        if difficulty == 1:
            kaef = 0.25
            break
        elif difficulty == 2:
            kaef = 0.35
            break
        elif difficulty == 3:
            kaef = 0.45
            break
        elif difficulty == 4:
            kaef = 0.55
            break
        else:
            difficulty = int(input('\n  Input Error! Please enter one of the options.\n> '))
    memory = []
    passcode = 0
    free = 0
    not_mines = 0
    fail = 0
    first = 5
    second = 5
    if time == 0:
        saper = Tk()
        saper.title('Sappy')
        razmer = N * 100 + 10
        razmer = str(razmer)
        razmer = str(razmer + "x" + razmer)
        saper.geometry(razmer)
        sappy = Canvas(saper, bg = 'white', width = N * 100 + 10, height = N * 100 + 10)
        sappy.pack()
        saper.resizable(width = False, height = False)
        saper.update()
    sappy.create_rectangle(5, 5, N * 100 + 5, N * 100 + 5, width = 10)
    saper.update()
    field = []
    randomnost = []
    for i in range(N * N):
        randomnost.append(0)
    for i in range(int((N * N) * kaef)):
        randomnost[i] = 1
    for i in range(10): shuffle(randomnost)
    mines = 0
    second = 5
    for i in range(N):
        field.append([])
        first = 5
        for j in range(N):
            field[i].append(randomnost[0]) 
            randomnost.remove(randomnost[0])
            if field[i][j] == 0:
                not_mines += 1
            else:
                mines += 1
            if i == 0:
                sappy.create_rectangle(5, 5, first + 100, second + 100, width = 4)
                saper.update()
            else:
                sappy.create_rectangle(first, second, first + 100, second + 100, width = 4)
                saper.update()
            if j == N - 1:
                second += 100
            else:
                first += 100
    if i != 0 and i != N - 1 and j != 0 and j != N - 1:
        if field[i - 1][j - 1] + field[i - 1][j] + field[i - 1][j + 1] + field[i][j - 1] + field[i][j + 1] + field[i + 1][j - 1] + field[i + 1][j] + field[i + 1][j + 1] > 5:
            field = []
    print('\n  Generated mines: ', mines, sep = "", end = ".\n")
    while free != not_mines and fail != 1:
        print('\n  Enter the coordinates of the field that you want to check.')
        while True:
            b = int(input('  X: '))
            a = int(input('  Y: '))
            if a > N or b > N or a < 1 or b < 1:
                print("\n  You have entered the wrong coordinates. Re-enter.")
                continue
            if [a,b] not in memory:
                break
            else:
                print('\n  You have already entered these coordinates! Enter the coordinates of the other.')
        memory.append([a,b])
        second = 5
        for i in range(N):
            first = 5
            for j in range(N):
                if i == a - 1 and j == b - 1:
                    if field[i][j] == 0:
                        if i != 0 and i != N - 1 and j != 0 and j != N - 1:
                            counted = field[i - 1][j - 1] + field[i - 1][j] + field[i - 1][j + 1] + field[i][j - 1] + field[i][j + 1] + field[i + 1][j - 1] + field[i + 1][j] + field[i + 1][j + 1]
                        elif i == 0 and j != 0 and j != N - 1:
                            counted = field[i][j - 1] + field[i][j + 1] + field[i + 1][j - 1] + field[i + 1][j] + field[i + 1][j + 1]
                        elif i == N - 1 and j != 0 and j != N - 1:
                            counted = field[i - 1][j - 1] + field[i - 1][j] + field[i - 1][j + 1] + field[i][j - 1] + field[i][j + 1]
                        elif i != 0 and i != N - 1 and j == 0:
                            counted = field[i - 1][j] + field[i + 1][j] + field[i - 1][j + 1] + field[i][j + 1] + field[i + 1][j + 1]
                        elif i != 0 and i != N - 1 and j == N - 1:
                            counted = field[i - 1][j - 1] + field[i - 1][j] + field[i][j - 1] + field[i + 1][j - 1] + field[i + 1][j]
                        elif i == 0 and j == 0:
                            counted = field[i][j + 1] + field[i + 1][j] + field[i + 1][j + 1]
                        elif i == 0 and j == N - 1:
                            counted = field[i][j - 1] + field[i + 1][j - 1] + field[i + 1][j]
                        elif i == N - 1 and j == 0:
                            counted = field[i - 1][j] + field[i - 1][j + 1] + field[i][j + 1]
                        elif i == N - 1 and j == N - 1:
                            counted = field[i - 1][j - 1] + field[i - 1][j] + field[i][j - 1]
                        sappy.create_text((first + 105) / 2, (second + 105) / 2, fill = "blue", font = ("arial", 18, "bold"), text = counted)
                        saper.update()
                        free += 1
                    else:
                        sappy.create_text((first + 105) / 2, (second + 105) / 2, fill = "yellow", font = ("arial", 18, "bold"), text = "BOMB")
                        saper.update()
                        fail = 1
                if j == N - 1:
                    second += 200
                else:
                    first += 200
    if fail == 1:
        print('\n  *BOOM*\n  You lose.')
        looses_in_row += 1
    if free == not_mines:                                                                
        print('\n  All the bombs defused!\n You won!')                            
        looses_in_row = 0
    memory_full = []
    for i in range(N):
        for j in range(N):
            memory_full.append([i + 1,j + 1])  
    for [a,b] in memory:
        memory_full.remove([a,b])
    for memory_perm in memory_full:
        second = 5
        for i in range(N):
            first = 5
            for j in range(N):
                if i == memory_perm[0] - 1 and j == memory_perm[1] - 1:
                    if field[i][j] == 0:
                        if i != 0 and i != N - 1 and j != 0 and j != N - 1:
                            counted = field[i - 1][j - 1] + field[i - 1][j] + field[i - 1][j + 1] + field[i][j - 1] + field[i][j + 1] + field[i + 1][j - 1] + field[i + 1][j] + field[i + 1][j + 1]
                        elif i == 0 and j != 0 and j != N - 1:
                            counted = field[i][j - 1] + field[i][j + 1] + field[i + 1][j - 1] + field[i + 1][j] + field[i + 1][j + 1]
                        elif i == N - 1 and j != 0 and j != N - 1:
                            counted = field[i - 1][j - 1] + field[i - 1][j] + field[i - 1][j + 1] + field[i][j - 1] + field[i][j + 1]
                        elif i != 0 and i != N - 1 and j == 0:
                            counted = field[i - 1][j] + field[i + 1][j] + field[i - 1][j + 1] + field[i][j + 1] + field[i + 1][j + 1]
                        elif i != 0 and i != N - 1 and j == N - 1:
                            counted = field[i - 1][j - 1] + field[i - 1][j] + field[i][j - 1] + field[i + 1][j - 1] + field[i + 1][j]
                        elif i == 0 and j == 0:
                            counted = field[i][j + 1] + field[i + 1][j] + field[i + 1][j + 1]
                        elif i == 0 and j == N - 1:
                            counted = field[i][j - 1] + field[i + 1][j - 1] + field[i + 1][j]
                        elif i == N - 1 and j == 0:
                            counted = field[i - 1][j] + field[i - 1][j + 1] + field[i][j + 1]
                        elif i == N - 1 and j == N - 1:
                            counted = field[i - 1][j - 1] + field[i - 1][j] + field[i][j - 1]
                        sappy.create_text((first + 105) / 2, (second + 105) / 2, fill = "green", font = ("arial", 18, "bold"), text = counted)
                        saper.update()
                    else:
                        sappy.create_text((first + 105) / 2, (second + 105) / 2, fill = "red", font = ("arial", 18, "bold"), text = "BOMB")
                        saper.update()
                if j == N - 1:
                    second += 200
                else:
                    first += 200
    answer = input('  You want to play with the current settings again(Y/N)?\n> ')
    while True:
        if answer not in ['Y','y','N','n']:
            answer = input('\n  Enter \"Y\" or \"N\", please.\n> ')
        else:
            break
    sappy.delete('all')
    time += 1
    system("cls")
input("  Press any key to continue . . . ")