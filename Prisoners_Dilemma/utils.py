import numpy as np
# The code is  Defect == 0
#              Cooperate == 1


def getPayOff(decisionGrid, reward):
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
    for i in range(dim[0]):
        for j in range(dim[1]):
            neighbours = oldDecision[i-1:i+1][j-1:j+1]
            winnerPos = np.unravel_index(neighbours.argmax(), neighbours.shape)
            newDecision[i][j] = oldDecision[i-1 + winnerPos[0]][j-1+winnerPos[1]]

    return newDecision



