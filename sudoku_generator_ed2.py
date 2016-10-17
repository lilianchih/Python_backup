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
if level == "easy":
    fout = open("sudoku_problems_easy", 'a')
    b = 45
elif level == "medium":
    fout = open("sudoku_problems_medium", 'a')
    b = 51
elif level == "hard":
    fout = open("sudoku_problems_hard", 'a')
    b = 57
else:
    fout = open("sudoku_problems_evil", 'a')
    b = 63
######## filling function ########
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
######## randomly filled grid ########
def generate_problem(b):
    sudoku = np.zeros([9, 9], dtype=int)
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
            random_numbers = range(1, 10)
            random.shuffle(random_numbers)
            for num in random_numbers:
                if fill(i, j, num, temp):
                    temptemp = np.copy(temp)
                    temptemp[i][j] = num
                    stack.append(temptemp)
        else:
            sudoku = temp
            break
    blanks = random.sample(range(81), b)
    for p in blanks:
        i = p / 9
        j = p % 9
        sudoku[i][j] = 0
    line = ""
    for i in range(9):
        for j in range(9):
            line += str(sudoku[i][j]) + " "
        line += "\n"

    stack = []
    answers = []
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
            else:
                filled = False
            i = position / 9
            j = position % 9
        if not filled:
            for num in range(9, 0, -1):
                if fill(i, j, num, temp):
                    temptemp = np.copy(temp)
                    temptemp[i][j] = num
                    stack.append(temptemp)
        else:
            answers.append(temp)
    if len(answers) == 0:
        print "No solution"
    else:
        for ans in answers:
            print ans
        if len(answers) == 1:
            fout.write("One solution\n")
        else:
            fout.write(str(len(answers)) + " solutions\n")
        fout.write(line + "\n")
x = raw_input("How many problems do you want?")
for i in range(int(x)):
    generate_problem(b)
fout.close()
