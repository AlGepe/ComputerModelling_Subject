import numpy as np
# import matplotlib
# matplotlib.use('pdf')
import matplotlib.pyplot as plt

# setup initial conditions
totalSteps = 50
koupling = 1.2
allCondt = [[3, 1.1], [3, 1.11], [3, 1.9], [3, 1.89]]
t = np.linspace(1, totalSteps, totalSteps)
j = 0
for initCond in allCondt:
    x = np.full(totalSteps, -1.)
    p = np.full(totalSteps, -1.)
    x[0] = initCond[0]
    p[0] = initCond[1]
    strNow = "Initial conditions: x0 = " + str(x[0]) + " || p0 = " + str(p[0])
    # plt.title(strNow)
    print(strNow)

    # for all steps
    for i in range(1, totalSteps):
        # Calculate new x, p
        p[i] = (p[i-1] + (koupling * np.sin(x[i-1]))) % (np.pi * 2)
        x[i] = (x[i-1] + p[i]) % (np.pi * 2)

    plt.subplot(2, 1, 1)
    plt.title("Momentum")
    plt.plot(t, p, '-', label='Momentum')
    plt.legend(loc=1)
    plt.grid(True)
    plt.subplot(2, 1, 2)
    plt.title("Position")
    plt.plot(t, x, '-', label='Position')
    plt.legend(loc='best')
    plt.grid(True)
    j += 1
    plt.savefig("stdPlot" + str(j) + ".png")
    plt.show()
