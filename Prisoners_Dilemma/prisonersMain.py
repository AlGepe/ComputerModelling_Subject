import os.path
import numpy as np
import utils as u
import matplotlib
# matplotlib.use('pdf')
import matplotlib.pyplot as plt

folder = os.path.abspath('./') + '/Data/'

#===============
# Common Values
#===============

sizeHalf = 100
N = (sizeHalf * 2) + 1
steps = 3

#==================
#    1st Task
#==================

rewardList = [1.9, 2.08]
for reward in rewardList:
    decisionGrid = np.ones(shape=(N, N))
    decisionGrid[sizeHalf][sizeHalf] = 0
    plt.figure(0, figsize=(7, 7))
    plt.clf()
    plt.figure(1, figsize=(7, 7))
    plt.clf()

    for i in range(steps):
        namePO = "Pay_Off_grid_{0:.2f}_{1:3d}".format(reward, i)
        nameDec = "Decision_grid_{0:.2f}_{1:3d}".format(reward, i)
        payOff = u.getPayOff(decisionGrid, reward)
        newdecisionGrid = u.updateDecisionGrid(decisionGrid, payOff)
        plt.figure(0)
        plt.imshow(payOff, interpolation='nearest', cmap=plt.cm.gray_r)
        if i == 1:
            plt.colorbar()
        plt.savefig(folder + namePO + '.png')
        toPlot = ((4 * np.logical_not(decisionGrid) *
                   np.logical_not(newdecisionGrid)) +
                  (1.5 * np.logical_not(decisionGrid) * newdecisionGrid) +
                  (0.25 * decisionGrid * np.logical_not(newdecisionGrid)))

        plt.figure(1)
        plt.imshow(toPlot, interpolation='nearest', cmap='gist_stern')
        if i == 1:
            plt.colorbar()
        decisionGrid = newdecisionGrid
        plt.savefig(folder + nameDec + '.png')


plt.figure(0)
plt.close()
plt.figure(1)
plt.close()
#=============
#   2nd Task
#=============

steps = 100
nRewards = 10
rewardMin = 0.5
rewardMax = 2.5
avg4reward = 5
rewardList = np.linspace(rewardMin, rewardMax, nRewards)
fPercentaje = np.zeros(shape=rewardList.shape)

for k in range(nRewards):
    decisionGrid = np.random.choice(2, size=(N, N))
    plt.figure(0, figsize=(7, 7))
    plt.clf()
    plt.figure(1, figsize=(7, 7))
    plt.clf()
    if not k % 5:
        print(k)

    reward_f = np.zeros(avg4reward)
    for j in range(avg4reward):
        for i in range(steps):
            # namePO = "Pay_Off_grid_{0:.2f}_{1:3d}".format(rewardList[k], i)
            payOff = u.getPayOff(decisionGrid, rewardList[k])
            newdecisionGrid = u.updateDecisionGrid(decisionGrid, payOff)
            # plt.figure(0)
            # plt.imshow(payOff, interpolation='nearest', cmap=plt.cm.gray_r)
            # if i == 1:
                # plt.colorbar()
            # plt.savefig(folder + namePO + '.png')
            toPlot = ((4 * np.logical_not(decisionGrid) *
                       np.logical_not(newdecisionGrid)) +
                      (1.5 * np.logical_not(decisionGrid) * newdecisionGrid) +
                      (0.25 * decisionGrid * np.logical_not(newdecisionGrid)))

            if i >= steps-5:
                nameDec = ("Decision_grid_{0:.2f}_{1:3d}".
                           format(rewardList[k], i))
                plt.figure(1)
                plt.imshow(toPlot, interpolation='nearest', cmap='gist_stern')
                if i == steps-5:
                    plt.colorbar()
                plt.savefig(folder + nameDec + '.png')
            decisionGrid = newdecisionGrid
            plt.clf()
            # i
        reward_f[j] = sum(sum(np.logical_not(decisionGrid)))
        # j
    fPercentaje[k] = np.average(reward_f) * 100 / np.square(N)
    # k

plt.figure(0)
plt.close()
plt.figure(1)
plt.close()

print("Done")
plt.figure(figsize=(16, 9))
plt.plot(rewardList, fPercentaje)
plt.show()
plt.savefig(folder + "f_of_b")
plt.close()
