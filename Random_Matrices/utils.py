import numpy as np


def createGOE(N):
    # allMatrices = np.empty(N, dtype=np.ndarray)
    # allMatrices.fill(forHam(np.random.randn(N, N)))
    a = np.random.randn(N, N)
    return (a + a.T) / 2


def createPM(N):
    matrix = (np.random.randint(2, size=(N, N)) * 2) - 1

    matrix = np.tril(matrix) + np.tril(matrix, -1).T
    for i in range(N):
        for j in range(i):
            matrix[i][j] = matrix[j][i]
    # print(matrix)
    return matrix  # symmetrize(np.random.randint(2, size=(N, N)))


# From Stackoverflow
def symmetrize(a):
    return a + a.T - np.diag(a.diagonal())


def wignerGOE(E, N):
    R = np.sqrt(2*N)
    # print(np.square(R) - np.square(E))
    return (2 * np.sqrt(np.square(R) - np.square(E)))/(np.pi * R * R)


def wignerPM(E, N):
    R = np.sqrt(4*N)
    # print(np.square(R) - np.square(E))
    return (2 * np.sqrt(np.square(R) - np.square(E)))/(np.pi * R * R)


def getEnergySpacing(eigen):
    preSpacing = np.diff(np.sort(eigen))
    return preSpacing / np.linalg.norm(preSpacing)


def surmise(eigenDiff):
    size = eigenDiff.shape
    # N = size[smth]
    N = size[0]
    indx = int(N/2)
    if N >= 10:
        # do this to each eigen spectrum, ie each matrix
        surmise = np.zeros(shape=(N, int(3.*N/8.)-int(5.*N/8.)))
    else:
        surmise = np.zeros(shape=(N,indx-1-indx+1))
    # s = 1

    for i in range(len(eigenDiff))
        if N >= 10:
            # do this to each eigen spectrum, ie each matrix
            s = eigenDiff[i][int(3.*N/8.):int(5.*N/8.)]
        else:
            s = eigenDiff[i][indx-1:indx+1]
        # s = 1
        surmise[i] = np.pi * .5 * s * np.exp(-(np.pi/4) * np.square(s))
    return surmise


def surmisePM(s):
    return
