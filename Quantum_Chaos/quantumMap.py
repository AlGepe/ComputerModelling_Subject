import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt


def prepGauss(M, x0, p0):
    # Define characteristics of WavePacket
    pi = np.pi
    # Convert to n, m
    n0 = M * x0 / (2 * pi)
    m0 = M * p0 / (2 * pi)

    # Do I need to convert x_n??

    n = np.arange(M)
    l_values = np.linspace(-4, 4, num=9)
    partSums = np.zeros(len(n))
    for l in l_values:
        tmp = np.square(n-n0 + M*l)
        partSums += np.exp((-pi/M) * (tmp))
    psi_Gn = partSums * np.exp((2j*pi*m0*n)/M)
    prob_dens = psi_Gn * np.conj(psi_Gn)
    psi_Gn = psi_Gn / np.linalg.norm(psi_Gn)
    x_n = (n * 2 * pi) / M
    plt.plot(x_n, psi_Gn, '+-', label='Amplitud')
    plt.plot(x_n, prob_dens, 'r+-', label='Probability Density')
    plt.plot(x0, 0, 'om', label='value of x0')
    plt.title("Wave Packet")
    plt.ylabel('Probability Density')
    plt.xlabel('x_n')
    plt.legend(loc=1)
    '''
    # plt.show()
    psi_Gm = fft(psi_Gn) / np.sqrt(M)
    plt.clf()
    probDens_m = psi_Gm * np.conj(psi_Gm)
    plt.plot(x_n, psi_Gm, '+-', label='Amplitud')
    plt.plot(x_n, probDens_m, 'r+-', label='Probability Density')
    plt.plot(p0, 0, 'om', label='value of p0')
    plt.title("Fourier Transform")
    plt.ylabel('Probability Density')
    plt.xlabel('p_n')
    plt.legend(loc=1)
    # plt.show()
    '''
    return psi_Gn


def oneStepFft(psi, K):
    # print(type(psi[0]))
    pi = np.pi
    M = len(psi)
    n = np.arange(M)
    bigP = np.exp((1j*np.square(n)*pi)/M)
    bigV = np.exp(-1j*M*K*np.cos((2*pi*n)/M)/2*pi)
    psi = (bigP * fft(bigP*bigV*psi)) / np.sqrt(M)
    return psi


def doIt(M, x0, p0, K, t_steps):
    pi = np.pi
    x_n = (np.arange(M) * 2 * pi) / M
    init = prepGauss(M, x0, p0)
    psi = np.zeros(shape=(t_steps, len(init)), dtype=complex)
    psi[0] = init
    plt.clf()
    plt.plot(x_n, psi[0]*np.conj(psi[0]), 'b+-')
    plt.axis([0, 2*pi, 0, 0.15])
    plt.savefig("Results/wave_packet" + str(0).zfill(3) + ".png")
    for t in range(t_steps-1):
        plt.clf()
        psi[t+1] = oneStepFft(psi[t], K)
        plt.plot(x_n, psi[t+1] * np.conj(psi[t+1]), 'b+-')
        plt.axis([0, 2*pi, 0, 0.15])
        plt.savefig("Results/wave_packet" + str(t).zfill(3) + ".png")
        # plt.show()


doIt(100, 3, 0.01, 2.1, 20)






