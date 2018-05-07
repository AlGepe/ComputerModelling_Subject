import numpy as np
import utils as u
import matplotlib
# matplotlib.use('pdf')
import matplotlib.pyplot as plt


sizeHalf = 10
N = (sizeHalf * 2) + 1
decisionGrid = np.zeros(shape=(N, N))
decisionGrid[sizeHalf-1][sizeHalf-1] = 1

for i in range(200):
    namePO = "Pay_Off_grid_" + str(i)
    nameDec = "Decision_grid_" + str(i)
    payOff = u.getPayOff(decisionGrid, 2.9)
    # print(decisionGrid.shape)
    decisionGrid = u.updateDecisionGrid(decisionGrid, payOff)
    # print(decisionGrid.shape)
    plt.imshow(payOff, interpolation='nearest', cmap=plt.cm.gray_r)
    # plt.show()
    # plt.savefig(namePO + '.png')
    plt.imshow(decisionGrid, interpolation='nearest', cmap=plt.cm.gray_r)
    plt.savefig(nameDec + '.png')
    plt.show()
