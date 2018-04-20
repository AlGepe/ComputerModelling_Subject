from utils import *
import numpy as np
#import matplotlib
#matplotlib.use('pdf')
import matplotlib.pyplot as plt

N = 10
n_sample = 10000

GOE_matrices = createGOE(N, n_sample)
# print(GOE_matrices.shape)
PM_matrices = createPM(N, n_sample)

'''
a = np.array([[1, -2j], [2j, 5]])
print(a.shape)
w, v = np.linalg.eigh(a)

print(type(GOE_matrices[0]))
print(type(np.random.normal(0, 1., size=(N, N))))
'''

GOE_eigVal, v = np.linalg.eigh(GOE_matrices)  # np.random.normal(0, 1., size=(N, N)))
PM_eigVal, v = np.linalg.eig(PM_matrices)

f, axarr = plt.subplots(2, sharex=True)
n, bins, patches = axarr[0].hist(GOE_eigVal, 50, normed=1,
        facecolor='green', alpha=0.75)
axarr[0].plot(bins, wignerGOE(bins, N), 'r-', linewidth=2)
n, bins, patches = axarr[1].hist(PM_eigVal, 50, normed=1,
        facecolor='green', alpha=0.75)
axarr[1].plot(bins, wignerPM(bins, N), 'r-', linewidth=2)

print(bins)

plt.show()
