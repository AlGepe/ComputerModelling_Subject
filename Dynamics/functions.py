import numpy as np

def squareLattice(N, L):
    lattice = np.zeros(shape=(N, N), dtype=np.ndarray)
    sites = np.linspace(0, L, N)
    for i in range(N):
        for j in range(N):
            lattice[i, j] = np.array([sites[i], sites[j]])
    return lattice
