import numpy as np
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
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

def doAll(reward, data):
    steps = data[0]
    avg4reward = data[1]
    N = data[2]
    folder = data[3]
    decisionGrid = np.random.choice(2, size=(N, N))
    plt.figure(0, figsize=(7, 7))
    plt.clf()
    plt.figure(1, figsize=(7, 7))
    plt.clf()
    stepsRward = int(1. / abs(reward - 2.)) + 50
    reward_f = np.zeros(avg4reward)
    for j in range(avg4reward):
        for i in range(stepsRward):
            # namePO = "Pay_Off_grid_{0:.2f}_{1:3d}".format(reward, i)
            payOff = getPayOff(decisionGrid, reward)
            newdecisionGrid = updateDecisionGrid(decisionGrid, payOff)
            # plt.figure(0)
            # plt.imshow(payOff, interpolation='nearest', cmap=plt.cm.gray_r)
                # plt.colorbar()
            # plt.savefig(folder + namePO + '.png')
            toPlot = ((4 * np.logical_not(decisionGrid) *
                    np.logical_not(newdecisionGrid)) +
                    (1.5 * np.logical_not(decisionGrid) * newdecisionGrid) +
                    (0.25 * decisionGrid * np.logical_not(newdecisionGrid)))

            if i >= stepsRward-5:
                nameDec = ("Decision_grid_{0:.2f}_{1:3d}".
                        format(reward, i))
                plt.figure(1)
                plt.imshow(toPlot, interpolation='nearest', cmap='gist_stern')
                if i == steps-5:
                    plt.colorbar()
                plt.savefig(folder + nameDec + '.png')
            decisionGrid = newdecisionGrid
            plt.clf()
            # i
        reward_f[j] = sum(sum(np.logical_not(decisionGrid)))
        # j
    return np.average(reward_f) * 100 / np.square(N)


def doAllCommunity(reward, data):
    steps = data[0]
    avg4reward = data[1]
    N = data[2]
    folder = data[3]
    communities = createCommunities(N, 0)
    decisionGrid = np.random.choice(2, size=(N, N))
    plt.figure(0, figsize=(7, 7))
    plt.clf()
    plt.figure(1, figsize=(7, 7))
    plt.clf()
    stepsRward = int(1. / abs(reward - 2.)) + 50
    payOff_total = np.zeros(shape=(stepsRward))
    payOff_j = np.zeros(shape=(avg4reward, stepsRward))
    for j in range(avg4reward):
        for i in range(stepsRward):
            # namePO = "Pay_Off_grid_{0:.2f}_{1:3d}".format(reward, i)
            payOff = getPayOff(decisionGrid, reward)
            newdecisionGrid = updateDecisionGrid(decisionGrid, payOff)
            if valueCom:
                decisionGrid = (newdecisionGrid * (not communities)) + communities
            else:
                decisionGrid = newdecisionGrid * communities
            if reward < 2 and reward > 1.9:
                payOff_j[j] = sum(sum((payOff))) / (N*N)
            # i
        payOff_total = np.average(payOff_j, axis=0)
        # j
    # plt.plot(range(stepsRward), payOff_total)
    # plt.savefig(folder + 'PayOff.png')
    # plt.close()
    # totalPO = np.average(payOff_f)
    return payOff_total




def doAllPayOff(reward, data):
    steps = data[0]
    avg4reward = data[1]
    N = data[2]
    folder = data[3]
    decisionGrid = np.random.choice(2, size=(N, N))
    plt.figure(0, figsize=(7, 7))
    plt.clf()
    plt.figure(1, figsize=(7, 7))
    plt.clf()
    stepsRward = int(1. / abs(reward - 2.)) + 50
    payOff_total = np.zeros(shape=(stepsRward))
    payOff_j = np.zeros(shape=(avg4reward, stepsRward))
    for j in range(avg4reward):
        for i in range(stepsRward):
            namePO = "Pay_Off_grid_{0:.2f}_{1:3d}".format(reward, i)
            payOff = getPayOff(decisionGrid, reward)
            newdecisionGrid = updateDecisionGrid(decisionGrid, payOff)
            decisionGrid = newdecisionGrid  # * communities
            if reward < 2 and reward > 1.9:
                payOff_j[j] = sum(sum((payOff))) / (N*N)
            # i
        payOff_total = np.average(payOff_j, axis=0)
        # j
    plt.plot(range(stepsRward), payOff_total)
    plt.savefig(folder + 'PayOff.png')
    plt.close()
    # totalPO = np.average(payOff_f)
    return payOff_total


def createCommunities(N, value):
    if value:
        communities = np.ones(N/10)
        decisionGrid = np.zeros(2, size=(N,N))
    else:
        community = np.zeros(N/10)
        decisionGrid = np.ones(2, size=(N,N))
    jArray = np.random.randint(N-12, size=5)
    for i in np.random.randint(N-12, size=5):
        j = jArray[i]
        decisionGrid[i:i+11][j:j+11] = community

    return decisionGrid



