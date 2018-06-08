import numpy as np
from matplotlib import pyplot as plt
import functions as f


T = 1
dt = 0.01
k = 1
N = 10
L = 1

# Create lattice(functions?)
# Square
# Triangle

# Simulate one step (function for that)



lattice = f.squareLattice(N, L)
for row in lattice:
    
    '''
    plt.plot(x[i:i+2], y[i:i+2], 'k-o')
plt.show()

plt.ion()
for i in range(50):
    y = np.random.random([10,1])
    plt.plot(y)
    plt.draw()
    plt.pause(0.0001)
    plt.clf()

'''
