import numpy as np
# The code is  Defect == 0
#              Cooperate == 1


def getPayOff_loop(decisionGrid, reward):
    dim = decisionGrid.shape
    payOff_grid = np.zeros(dim)
    for i in range(dim[0]):
        for j in range(dim[1]):
            neighSum = decisionGrid[i+1][j] + decisionGrid[i-1][j] +\
                    decisionGrid[i+1][j+1] + decisionGrid[i][j+1] +\
                    decisionGrid[i-1][j+1] + decisionGrid[i+1][j-1] +\
                    decisionGrid[i][j-1] + decisionGrid[i-1][j-1] +\
                    decisionGrid[i][j]
            if decisionGrid[i][j]:
                payOff_grid[i][j] = neighSum
            else:
                payOff_grid[i][j] = (8 - neighSum) * reward
    return payOff_grid


def updateDecisionGrid(oldDecision, payOff_grid):
    dim = oldDecision.shape
    newDecision = np.zeros(dim)
    for i in range(1, dim[0]-1):
        for j in range(1, dim[1]-1):
            neighbours = oldDecision[i-1:i+1, j-1:j+1]
            #print(neighbours)
            winnerPos = np.unravel_index(neighbours.argmax(), neighbours.shape)
            newDecision[i][j] = oldDecision[i-1 + winnerPos[0]][j-1+winnerPos[1]]

    return newDecision


def getPayOff(decisionGrid, reward):
    # sum == how many neighbours did C
    b = 8
    sumGrid = (decisionGrid +
               shiftPB(decisionGrid, [ 1,  1]) +
               shiftPB(decisionGrid, [ 1,  0]) + 
               shiftPB(decisionGrid, [ 1, -1]) +
               shiftPB(decisionGrid, [ 0,  1]) +
               shiftPB(decisionGrid, [ 0, -1]) +
               shiftPB(decisionGrid, [-1, 1]) +
               shiftPB(decisionGrid, [-1, 0]) +
               shiftPB(decisionGrid, [-1, -1]))
    payOff = sumGrid * decisionGrid  # CC = +1
    payOff += (decisionGrid == 0) * ((sumGrid) * b)  # DC = b
    return payOff


def shiftPB(original, shift):
    shifted = np.zeros(original.shape)
    i = shift[0]
    j = shift[1]
    if j == 0:
        shifted[i:, :] = original[:-i, :]
        # shifted[i:, :] = original[i:, -j:]
        shifted[:i, j:] = original[-i:, j:]
        #shifted[:i, :] = original[-i:, -j:]

    elif i == 0:
        shifted[i:, j:] = original[:, :-j]
        shifted[i:, :j] = original[i:, -j:]
        # shifted[:i, j:] = original[-i:, j:]
        #shifted[:i, :j] = original[-i:, -j:]

    else:
        shifted[i:, j:] = original[:-i, :-j]
        shifted[i:, :j] = original[i:, -j:]
        shifted[:i, j:] = original[-i:, j:]
        shifted[:i, :j] = original[-i:, -j:]
    return shifted
    


