import matplotlib.pyplot as plt
import numpy as np

for i in range(4):
    plt.axvline(x = 3*i, linewidth = 3, color = 'k')
    plt.axhline(y = 3*i, linewidth = 3, color = 'k')
for i in range(10):
    plt.axvline(x = i, linewidth = 1, color = 'k')
    plt.axhline(y = i, linewidth = 1, color = 'k')

sudoku = np.empty([9, 9], dtype = int)
for i in range(9):
    cin = raw_input("")
    l = cin.split()
    for j in range(9):
        sudoku[i][j] = int(l[j])

for i in range(9):
    for j in range(9):
        if sudoku[i][j] != 0:
            plt.text(j+0.35, 8-i+0.35, str(sudoku[i][j]), size=18)

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
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == 0:
                    plt.text(j+0.35, 8-i+0.35, str(temp[i][j]), size=18, color='r')
        break

#plt.axis('off')
plt.axis('scaled')
plt.tick_params(which='both', top='off', bottom='off', left='off', right='off', labelbottom='off', labelleft='off')

plt.show()
