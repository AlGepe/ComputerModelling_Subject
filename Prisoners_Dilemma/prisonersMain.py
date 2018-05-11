import os.path
import numpy as np
import utils as u
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt

folder = os.path.abspath('./') + '/Data/'


sizeHalf = 100
N = (sizeHalf * 2) + 1
decisionGrid = np.ones(shape=(N, N))
decisionGrid[sizeHalf][sizeHalf] = 0
plt.figure(figsize=(10, 10))
plt.imshow(decisionGrid, interpolation='nearest', cmap='gist_stern')
# print(decisionGrid)

for i in range(200):
    namePO = folder + "Pay_Off_grid_" + str(i)
    nameDec = folder + "Decision_nochange_" + str(i)
    payOff = u.getPayOff(decisionGrid, 2.08)
    newdecisionGrid = u.updateDecisionGrid(decisionGrid, payOff)
    plt.imshow(payOff, interpolation='nearest', cmap=plt.cm.gray_r)
    toPlot = ((4 * np.logical_not(decisionGrid) * np.logical_not(newdecisionGrid)) +
              (1.5 * np.logical_not(decisionGrid) * newdecisionGrid) +
              (0.25 * decisionGrid * np.logical_not(newdecisionGrid)))

    plt.imshow(toPlot, interpolation='nearest', cmap='gist_stern')

    if i == 1:
        plt.colorbar()
    decisionGrid = newdecisionGrid
    plt.savefig(nameDec + '.png')
