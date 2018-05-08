import os.path
import numpy as np
import utils as u
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt

folder = os.path.abspath('./') + '/Data/Results/'


sizeHalf = 100
N = (sizeHalf * 2) + 1
decisionGrid = np.ones(shape=(N, N))
decisionGrid[sizeHalf][sizeHalf] = 0
# print(decisionGrid)

for i in range(200):
    namePO = folder + "Pay_Off_grid_" + str(i)
    nameDec = folder + "Decision_grid_" + str(i)
    payOff = u.getPayOff(decisionGrid, 1.94)
    # print(payOff)
    # print(payOff)
    # print(decisionGrid.shape)
    decisionGrid = u.updateDecisionGrid(decisionGrid, payOff)
    # print(decisionGrid.shape)
    plt.imshow(payOff, interpolation='nearest', cmap=plt.cm.gray_r)
    # plt.show()
    # plt.show()
    # plt.savefig(namePO + '.png')
    plt.imshow(decisionGrid, interpolation='nearest', cmap=plt.cm.gray_r)
    # print(decisionGrid)
    plt.savefig(nameDec + '.png')
