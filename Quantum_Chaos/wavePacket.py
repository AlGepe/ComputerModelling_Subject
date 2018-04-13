import numpy as np
import matplotlib.pyplot as plt


def prepGauss(x_n):
    # Define characteristics of WavePacket
    M = 100
    x0 = 3
    p0 = 1.1
    pi = np.pi
    # Convert to n, m
    n0 = M * x0 * 2 * pi
    m0 = M * p0 * 2 * pi

    '''
    Do I need to convert x_n??
    '''

    n_max = 2*pi - (2*pi/M)
    n = np.linspace(0, n_max, num=M)
    l_values = np.linspace(-4, 4, num=9)
    partSums = np.zeros(100)
    for l in l_values:
        tmp = np.square(n-n0 + M*l)
        partSums = partSums + np.exp((-pi/M) * (tmp))
    print(partSums[3])
    psi_n = partSums * np.exp((2j*pi*m0*n)/M)
    prob_dens = psi_n * np.conj(psi_n)
    big_N = sum(prob_dens)
    psi_n = big_N * psi_n
    prob_dens = psi_n * np.conj(psi_n)
    print(big_N.real)
    plt.plot(n, prob_dens, '+')
    plt.plot(x0, 0, '+m')
    plt.show()
    return psi_n[x_n]/big_N


prepGauss(3)
