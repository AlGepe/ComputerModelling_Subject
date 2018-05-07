from utils import *
import numpy as np
#import matplotlib
#matplotlib.use('pdf')
import matplotlib.pyplot as plt

N = 10
n_sample = 1000

f, axarr = plt.subplots(2, sharex=True)
GOE_eigVal = np.zeros(shape=(n_sample, N))
PM_eigVal = np.zeros(shape=(n_sample, N))

for i in range(n_sample):
    GOE_matrices = createGOE(N)
    PM_matrices = createPM(N)
    # print(np.all(PM_matrices == PM_matrices.T))

    GOE_eigVal[i] = np.linalg.eigvalsh(GOE_matrices)
    PM_eigVal[i]  = np.linalg.eigvalsh(PM_matrices)

n, bins, patches = axarr[0].hist(GOE_eigVal.flatten(), 50, density=True,
                                 facecolor='green', alpha=0.75)
n, bins, patches = axarr[1].hist(PM_eigVal.flatten(), 50, density=True,
                                 facecolor='blue', alpha=0.75)
axarr[1].plot(bins, wignerPM(bins, N), 'r-', linewidth=2)
axarr[0].plot(bins, wignerGOE(bins, N), 'r-', linewidth=2)

# print(bins)
plt.show()
