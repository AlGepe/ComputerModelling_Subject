import numpy as np
# import matplotlib.pyplot as plt
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
    # print(oldDecision)
    oldDecisionPB = np.zeros(np.asarray(dim) + 2)
    # inner square
    oldDecisionPB[1:-1, 1:-1] = oldDecision
    # top-bottom
    oldDecisionPB[0:1,  1:-1] = oldDecision[-1:, :]  # top
    oldDecisionPB[-1:,  1:-1] = oldDecision[:1, :]  # bottom
    # R-L sides
    oldDecisionPB[:, 0:1] = oldDecisionPB[:, -2:-1]
    oldDecisionPB[:, -1:] = oldDecisionPB[:, 1:2]
    newDecision = np.zeros(oldDecisionPB.shape)

    payOff_PB = np.zeros(np.asarray(dim) + 2)
    # inner square
    payOff_PB[1:-1, 1:-1] = payOff_grid
    # top-bottom
    payOff_PB[0:1,  1:-1] = payOff_grid[-1:, :]  # top
    payOff_PB[-1:,  1:-1] = payOff_grid[:1, :]  # bottom
    # R-L sides
    payOff_PB[:, 0:1] = payOff_PB[:, -2:-1]
    payOff_PB[:, -1:] = payOff_PB[:, 1:2]
    for i in range(1, dim[0]+1):
        for j in range(1, dim[1]+1):
            neighbours = payOff_PB[i-1:i+2, j-1:j+2]
            winnerPos = np.unravel_index(neighbours.argmax(), neighbours.shape)
            newDecision[i][j] = oldDecisionPB[i-1 + winnerPos[0],
                                              j-1 + winnerPos[1]]

    return newDecision[1:dim[0] + 1, 1:dim[1] + 1]


def getPayOff(decisionGrid, reward=8):
    # sumGrid == how many neighbours did C(ooperate)
    sumGrid = (decisionGrid +
               shiftPB(decisionGrid, [ 1,  1]) +
               shiftPB(decisionGrid, [ 1,  0]) +
               shiftPB(decisionGrid, [ 1, -1]) +
               shiftPB(decisionGrid, [ 0,  1]) +
               shiftPB(decisionGrid, [ 0, -1]) +
               shiftPB(decisionGrid, [-1, 1]) +
               shiftPB(decisionGrid, [-1, 0]) +
               shiftPB(decisionGrid, [-1, -1]))
    payOff = sumGrid * decisionGrid * 1.0  # CC = +1
    payOff += (decisionGrid == 0) * ((sumGrid) * reward)  # DC = b
    return payOff


def shiftPB(original, shift):
    shifted = np.zeros(original.shape, dtype=type(original[0,0]))
    i = shift[0]
    j = shift[1]
    if j == 0 and i == 0:
        return original
    elif j == 0:
        shifted[i:, :] = original[:-i, :]
        shifted[:i, :] = original[-i:, :]

    elif i == 0:
        shifted[:, j:] = original[:, :-j]
        shifted[:, :j] = original[:, -j:]

    else:
        # Big Square (for big N and small shifts)
        shifted[i:, j:] = original[:-i, :-j]
        # Small Square (for big N and small shifts)
        shifted[:i, :j] = original[-i:, -j:]
        # 'Bottom slice' for positive i and j
        shifted[:i, j:] = original[-i:, :-j]
        # 'Right slide' (for positive i and j)
        shifted[i:, :j] = original[:-i, -j:]
    return shifted
