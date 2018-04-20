import numpy as np


def createGOE(N):
    # allMatrices = np.empty(N, dtype=np.ndarray)
    # allMatrices.fill(forHam(np.random.randn(N, N)))
    return forHam(np.random.randn(N, N))


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
    return (2 * np.sqrt(np.square(R) - np.square(E)))/(np.pi * R * R)


def wignerPM(E, N):
    R = np.sqrt(4*N)
    return (2 * np.sqrt(np.square(R) - np.square(E)))/(np.pi * R * R)


def forHam(a):
    return (a + a.T) / 2


def getEnergySpacing(eigen):
    return np.diff(np.sort(eigen))
