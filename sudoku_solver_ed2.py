import numpy as np

######## initialize sudoku ########
sudoku = np.empty([9, 9], dtype = int)
for i in range(9):
    cin = raw_input("")
    l = cin.split()
    for j in range(9):
        sudoku[i][j] = int(l[j])
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
######## guess numbers ########
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

print sudoku

