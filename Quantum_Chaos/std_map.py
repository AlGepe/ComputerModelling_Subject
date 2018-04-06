import numpy as np
# import matplotlib
# matplotlib.use('pdf')
import matplotlib.pyplot as plt

# setup initial conditions
totalSteps = 1000
kouplingList = [1.2, 2.1, 5.5]
for koupling in kouplingList:
    print("Coupling constant: K = " + str(koupling))
    allCondt = np.random.rand(100, 2)
    allCondt *= 2 * np.pi
    for initCond in allCondt:
        r, g, b = np.random.ranf(3)
        x = np.full(totalSteps, -1.)
        p = np.full(totalSteps, -1.)
        x[0] = initCond[0]
        p[0] = initCond[1]
        strNow = "Initial conditions: x0 = " + str(x[0]) + \
            " || p0 = " + str(p[0])
        # plt.title(strNow)
        # print(strNow)

        # for all steps
        for i in range(1, totalSteps):
            # Calculate new x, p
            p[i] = (p[i-1] + (koupling * np.sin(x[i-1]))) % (np.pi * 2)
            x[i] = (x[i-1] + p[i]) % (np.pi * 2)

        plt.plot(x, p, ',', color=(r, g, b))
    plt.savefig("stdMap_coupling" + str(koupling) + ".png")
    plt.show()
