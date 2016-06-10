import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(6,6), dpi=100)
ax = plt.axes()

textes = []
for i in range(9):
    text = []
    for j in range(9):
        tex = ax.text(j+0.35, 8-i+0.35, '', size=18, color='r')
        text.append(tex)
    textes.append(text)

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

def init():
    for i in range(9):
        for j in range(9):
            textes[i][j].set(text='')
    return textes[0][0], textes[0][1], textes[0][2], textes[0][3], textes[0][4], textes[0][5], textes[0][6], textes[0][7], textes[0][8], textes[1][0], textes[1][1], textes[1][2], textes[1][3], textes[1][4], textes[1][5], textes[1][6], textes[1][7], textes[1][8], textes[2][0], textes[2][1], textes[2][2], textes[2][3], textes[2][4], textes[2][5], textes[2][6], textes[2][7], textes[2][8], textes[3][0], textes[3][1], textes[3][2], textes[3][3], textes[3][4], textes[3][5], textes[3][6], textes[3][7], textes[3][8], textes[4][0], textes[4][1], textes[4][2], textes[4][3], textes[4][4], textes[4][5], textes[4][6], textes[4][7], textes[4][8], textes[5][0], textes[5][1], textes[5][2], textes[5][3], textes[5][4], textes[5][5], textes[5][6], textes[5][7], textes[5][8], textes[6][0], textes[6][1], textes[6][2], textes[6][3], textes[6][4], textes[6][5], textes[6][6], textes[6][7], textes[6][8], textes[7][0], textes[7][1], textes[7][2], textes[7][3], textes[7][4], textes[7][5], textes[7][6], textes[7][7], textes[7][8], textes[8][0], textes[8][1], textes[8][2], textes[8][3], textes[8][4], textes[8][5], textes[8][6], textes[8][7], textes[8][8]

stack = []
stack.append(sudoku)
filled = False
frames = []

while len(stack) != 0:
    temp = stack[-1]
    frames.append(temp)
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
        break

c = 0
def animate(i):
    global c
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                if frames[c][i][j] != 0:
                    textes[i][j].set(text=str(frames[c][i][j]))
                else:
                    textes[i][j].set(text='')
    if c < len(frames) - 1:
        c += 1
    return textes[0][0], textes[0][1], textes[0][2], textes[0][3], textes[0][4], textes[0][5], textes[0][6], textes[0][7], textes[0][8], textes[1][0], textes[1][1], textes[1][2], textes[1][3], textes[1][4], textes[1][5], textes[1][6], textes[1][7], textes[1][8], textes[2][0], textes[2][1], textes[2][2], textes[2][3], textes[2][4], textes[2][5], textes[2][6], textes[2][7], textes[2][8], textes[3][0], textes[3][1], textes[3][2], textes[3][3], textes[3][4], textes[3][5], textes[3][6], textes[3][7], textes[3][8], textes[4][0], textes[4][1], textes[4][2], textes[4][3], textes[4][4], textes[4][5], textes[4][6], textes[4][7], textes[4][8], textes[5][0], textes[5][1], textes[5][2], textes[5][3], textes[5][4], textes[5][5], textes[5][6], textes[5][7], textes[5][8], textes[6][0], textes[6][1], textes[6][2], textes[6][3], textes[6][4], textes[6][5], textes[6][6], textes[6][7], textes[6][8], textes[7][0], textes[7][1], textes[7][2], textes[7][3], textes[7][4], textes[7][5], textes[7][6], textes[7][7], textes[7][8], textes[8][0], textes[8][1], textes[8][2], textes[8][3], textes[8][4], textes[8][5], textes[8][6], textes[8][7], textes[8][8]

#plt.axis('off')
plt.axis('scaled')
plt.tick_params(which='both', top='off', bottom='off', left='off', right='off', labelbottom='off', labelleft='off')

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=10, interval=40)
plt.show()