# AoC 22
import math
file = open("input_22.txt",'r')
#file = open("tmp.txt",'r')

lines = [line.rstrip() for line in file.readlines()]

gridSize = 501
grid = [['.' for i in range(gridSize)] for j in range(gridSize)]
gridB = [['.' for i in range(gridSize)] for j in range(gridSize)]



nrofCols = lines[0].__len__()
nrofRows = lines.__len__()

startC = int((gridSize-1) / 2 - (nrofCols-1)/2)
startR = int((gridSize-1) / 2 - (nrofRows-1)/2)
for c in range(startC,startC+nrofCols):
    for r in range(startR,startR+nrofRows):
        grid[r][c]  = lines[r - startR][c - startC]
        gridB[r][c] = lines[r - startR][c - startC]

pos_x = int((gridSize-1) / 2)
pos_y = int((gridSize-1) / 2)

bursts = 10000
dir = 0
infected = 0
for b in range(bursts):
   # print(pos_x,pos_y)
    turn = 'r' if grid[pos_x][pos_y]=='#' else 'l'
    grid[pos_x][pos_y] = '#' if grid[pos_x][pos_y] == '.' else '.'

    # move
    dir += 90 if turn =='r' else -90
    if(grid[pos_x][pos_y] =='#'):
        infected += 1
    pos_x -= int(math.cos((dir/180)*math.pi))
    pos_y += int(math.sin((dir / 180) * math.pi))

print(" A = ",infected)

## Solve B
pos_x = int((gridSize-1) / 2)
pos_y = int((gridSize-1) / 2)

bursts = 10000000
dir = 0
infected_b = 0
for b in range(bursts):
    nextGrid = ''

    if gridB[pos_x][pos_y]=='#':
        dir += 90
        nextGrid = 'F'

    elif gridB[pos_x][pos_y]=='.':
        dir -= 90
        nextGrid = 'W'

    elif gridB[pos_x][pos_y]=='F':
        dir += 180
        nextGrid = '.'
    else:
        nextGrid = '#'

    gridB[pos_x][pos_y] = nextGrid

    if(gridB[pos_x][pos_y] =='#'):
        infected_b += 1
    pos_x -= int(math.cos((dir/180)*math.pi))
    pos_y += int(math.sin((dir / 180) * math.pi))

print('Infected B ',infected_b)