import numpy as np
import random

######## enter level ########
correct = False
while not correct:
    level = raw_input("Which level do you want to challenge? (easy/ medium/ hard/ evil) ")
    if level != "easy" and level != "medium" and level != "hard" and level != "evil":
        print "Please input level again."
        correct = False
    else:
        correct = True
######## checking function ########
def fill(i, j, num, su):
    for row in range(9):
        if su[row][j] == num:
            return False
    for col in range(9):
        if su[i][col] == num:
            return False
    m = (i/3) * 3
    n = (j/3) * 3
    for row in range(3):
        for col in range(3):
            if su[m+row][n+col] == num:
                return False
    return True
######## save to file ########
fout = open("sudoku_problems", 'a')
######## search for solvable problems ########
def search():
    solvable = False
    while not solvable:
        ######## initialize sudoku ########
        contradict = True
        while contradict:
            sudoku = np.zeros([9, 9], dtype=int)
            if level == "easy":
                problem = random.sample(range(81), 36)
                correct = True
            elif level == "medium":
                problem = random.sample(range(81), 30)
                correct = True
            elif level == "hard":
                problem = random.sample(range(81), 24)
                correct = True
            elif level == "devil":
                problem = random.sample(range(81), 18)
                correct = True
            contradict = False
            for p in problem:
                i = p / 9
                j = p % 9
                poss_num = []
                for n in range(1, 10):
                    if fill(i, j, n, sudoku):
                        poss_num.append(n)
                if len(poss_num) != 0:
                    sudoku[i][j] = random.choice(poss_num)
                else:
                    contradict = True
                    #print "Contradiction!"
                    break
        line = ""
        for i in range(9):
            for j in range(9):
                line += str(sudoku[i][j]) + " "
            line += "\n"
        ######## solve ########
        stack = []
        stack.append(sudoku)
        filled = False
        while len(stack) != 0:
            temp = stack[-1]
            del stack[-1]
            position = 0
            i, j = 0, 0
            while temp[i][j] != 0:
                position += 1
                if position == 81:
                    filled = True
                    break
                i = position / 9
                j = position % 9
            if not filled:
                for num in range(1, 10):
                    if fill(i, j, num, temp):
                        temptemp = np.copy(temp)
                        temptemp[i][j] = num
                        stack.append(temptemp)
            else:
                sudoku = temp
                break
        if not filled:
            pass
            #print "No answer!"
        else:
            solvable = True
            print sudoku
            fout.write(line + "\n")
for i in range(10):
    search()
fout.close()





