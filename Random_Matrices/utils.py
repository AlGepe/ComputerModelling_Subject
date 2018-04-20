import numpy as np


def createGOE(N, n_sample):
    allMatrices = np.full((n_sample, N, N),
            forHam(np.random.randn(N, N)))
    return allMatrices


def createPM(N, n_sample):
    allMatrices = np.full((n_sample, N, N),
            symmetrize(np.random.randint(2, size=(N, N))))
    return allMatrices


# From Stackoverflow
def symmetrize(a):
    return a + a.T - np.diag(a.diagonal())

def wignerGOE(E, N):
    R = np.sqrt(2*N)
    return (2 * np.sqrt(np.square(R) - np.square(E)))/(np.pi * R * R)

def wignerPM(E, N):
    R = np.sqrt(4*N)
    return (2 * np.sqrt(np.square(R) - np.square(E)))/(np.pi * R * R)

def forHam(a):
    return (a + a.T) / 2
