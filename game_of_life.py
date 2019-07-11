#!/usr/bin/python3

import sys
from copy import deepcopy

def getGrid(fname):
    array2D = []
    with open(fname, 'r') as f:
        for line in f.readlines():
            if '\n' in line:
                array2D.append(list(line.rstrip()))
            else:
                array2D.append(list(line))

    return array2D

def printGrid(generationNumber, array2D):
    for line in array2D:
        print (''.join(line))

    print ("Generation: ", generationNumber)

def computeGeneration(array2D):
    X = len(array2D)
    Y = len(array2D[0])
    newArray2D = deepcopy(array2D)

    for x in range(X):
        for y in range(Y):
            numberOfStars = nei(x,y,array2D,X,Y).count("*")
            if array2D[x][y] == '*' and numberOfStars < 2:
                #umira v osamoceni
                newArray2D[x][y] = '.'
            elif array2D[x][y] == '*' and numberOfStars > 3:
                #umira preplnenim
                newArray2D[x][y] = '.'
            elif array2D[x][y] == '*' and (numberOfStars == 2 or numberOfStars == 3):
                #preziva
                newArray2D[x][y] = '*'
            elif array2D[x][y] == '.' and numberOfStars == 3:
                #oziva
                newArray2D[x][y] = '*'
            else:
                #nic
                newArray2D[x][y] = array2D[x][y]

    return newArray2D


def nei(x,y,array,height,width):
    neiArray = []
    for x_ in range(max(0, x - 1), min(height, x + 2)):
        for y_ in range(max(0, y - 1), min(width, y + 2)):
            if (x, y) == (x_, y_): continue
            neiArray.append(array[x_][y_])

    return neiArray

if __name__== "__main__":
    grid = getGrid(sys.argv[1])

    for i in range(10):
        printGrid(i + 1, grid)
        grid = computeGeneration(grid)
