import numpy as np
# import matplotlib
# matplotlib.use('pdf')
import matplotlib.pyplot as plt


decisionGrid = np.zeros(shape=(21, 21))
decisionGrid[10][10] = 1

plt.imshow(decisionGrid, interpolation='nearest', cmap=plt.cm.gra_r)
plt.show()

