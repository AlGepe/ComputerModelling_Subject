import numpy as np
import utils as u
# import matplotlib
# matplotlib.use('pdf')
import matplotlib.pyplot as plt


decisionGrid = np.zeros(shape=(22, 22))
decisionGrid[10][10] = 1

for i in range(20):
    payOff = u.getPayOff(decisionGrid, 3)
    decisionGrid = u.updateDecisionGrid(decisionGrid, payOff)
    plt.imshow(decisionGrid, interpolation='nearest', cmap=plt.cm.gray_r)
    plt.show()
