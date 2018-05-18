import os.path
import multiprocessing
from functools import partial
import time
import numpy as np
import utils as u
import matplotlib
# matplotlib.use('pdf')
import matplotlib.pyplot as plt

folder = os.path.abspath('./') + '/Data1/'

#===============
# Common Values
#===============

t0 = time.time()
sizeHalf = 100
N = (sizeHalf * 2) + 1
steps = 200

#==================
#    1st Task
#==================

rewardList = [1.9, 2.00, 2.08]
for reward in rewardList:
    decisionGrid = np.ones(shape=(N, N))
    decisionGrid[sizeHalf][sizeHalf] = 0
    plt.figure(0, figsize=(7, 7))
    plt.clf()
    plt.figure(1, figsize=(7, 7))
    plt.clf()

    for i in range(steps):
        namePO = "Pay_Off_grid_{0:.2f}_{1:03d}".format(reward, i)
        nameDec = "Decision_grid_{0:.2f}_{1:03d}".format(reward, i)
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
t1 = time.time()
print("Finished task 1 in {0}seconds".format(t1-t0))
#=============
#   2nd Task
#=============
folder = os.path.abspath('./') + '/Data2/'

steps = 100
nRewards = 50
rewardMin = 1.9
rewardMax = 2.1
avg4reward = 5
rewardList = np.linspace(rewardMin, rewardMax, nRewards)
rewardList[0] = 0.5
rewardList[1] = 1.0
rewardList[2] = 1.5
rewardList[nRewards-1] = 2.5
fPercentaje = np.zeros(shape=rewardList.shape)
myData = [steps, avg4reward, N, folder]

decisionGrid = np.random.choice(2, size=(N, N))
plt.figure(0, figsize=(7, 7))
plt.clf()
plt.figure(1, figsize=(7, 7))
plt.clf()
num_cores = int(multiprocessing.cpu_count()-1)

plt.figure(0)
plt.close()
plt.figure(1)
plt.close()

print("Data setup")
with multiprocessing.Pool(processes=num_cores) as pool:
    do_all_grids = partial(u.doAll, data = myData)
    print("function partialised")
    fPercentaje = pool.map(do_all_grids, rewardList)

t2 = time.time()
print("Task 2 done in {0}seconds".format(t2-t1))
np.savez_compressed(folder+"data2.npz", x=rewardList, y=fPercentaje)
plt.figure(figsize=(16, 9))
plt.plot(rewardList, fPercentaje)
# plt.plot(rewardList, poTotal)
plt.axis([0, 3., -1, 101])
# plt.show()
plt.savefig(folder + "f_of_b")
plt.close()
t3 = time.time()
print("All done in {0}seconds".format(t3-t0))

#=============
#   3rd Task
#=============

'''dd
steps = 100
nRewards = 10
rewardMin = 1.9
rewardMax = 2.1
avg4reward = 5
rewardList = np.linspace(rewardMin, rewardMax, nRewards)
rewardList[0] = 0.5
rewardList[1] = 1.0
rewardList[2] = 1.5
rewardList[nRewards-1] = 2.5
fPercentaje = np.zeros(shape=rewardList.shape)
myData = [steps, avg4reward, N, folder]

decisionGrid = np.random.choice(2, size=(N, N))
plt.figure(0, figsize=(7, 7))
plt.clf()
plt.figure(1, figsize=(7, 7))
plt.clf()
num_cores = int(multiprocessing.cpu_count())

plt.figure(0)
plt.close()
plt.figure(1)
plt.close()

print("Data setup")
with multiprocessing.Pool(processes=num_cores) as pool:
    do_all_grids = partial(u.doAllPayOff, data = myData)
    print("function partialised")
    payOffArray = pool.map(do_all_grids, rewardList)

t2 = time.time()
print("Task 2 done in {0}seconds".format(t2-t1))
np.savez_compressed('PayOff_data', payOffArray)
plt.figure(figsize=(16, 9))
print(len(payOffArray))
print(type(payOffArray[0]))
for i in range(nRewards):
    plt.plot(range(len(payOffArray[i])), payOffArray[i], label=str(rewardList[i]))
# plt.plot(rewardList, poTotal)
# plt.axis([0, 3., -1, 101])
plt.legend()
plt.savefig(folder + "payOff_time.png")
plt.show()
# plt.close()
t3 = time.time()
print("All done in {0}seconds".format(t3-t0))
'''
'''
#=============
#   2nd Task
#=============

steps = 100
nRewards = 20
rewardMin = 1.9
rewardMax = 2.1
avg4reward = 5
rewardList = np.linspace(rewardMin, rewardMax, nRewards)
rewardList[0] = 0.5
rewardList[1] = 1.0
rewardList[2] = 1.5
rewardList[nRewards-1] = 2.5
fPercentaje = np.zeros(shape=rewardList.shape)

for k in range(nRewards):
    decisionGrid = np.random.choice(2, size=(N, N))
    plt.figure(0, figsize=(7, 7))
    plt.clf()
    plt.figure(1, figsize=(7, 7))
    plt.clf()
    stepsRward = int(1. / abs(rewardList[k] - 2.)) + 50
    if not k % 5:
        print("Iteration number: {0} of {1}".format(k, nRewards))
        print("Reward: {0}".format(rewardList[k]))
        print("Steps: {0}\n".format(stepsRward))

    reward_f = np.zeros(avg4reward)
    for j in range(avg4reward):
        for i in range(stepsRward):
            # namePO = "Pay_Off_grid_{0:.2f}_{1:3d}".format(rewardList[k], i)
            payOff = u.getPayOff(decisionGrid, rewardList[k])
            newdecisionGrid = u.updateDecisionGrid(decisionGrid, payOff)
            # plt.figure(0)
            # plt.imshow(payOff, interpolation='nearest', cmap=plt.cm.gray_r)
                # plt.colorbar()
            # plt.savefig(folder + namePO + '.png')
            toPlot = ((4 * np.logical_not(decisionGrid) *
                       np.logical_not(newdecisionGrid)) +
                      (1.5 * np.logical_not(decisionGrid) * newdecisionGrid) +
                      (0.25 * decisionGrid * np.logical_not(newdecisionGrid)))

            if i >= stepsRward-5:
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
plt.axis([0, 3., -1, 101])
# plt.show()
plt.savefig(folder + "f_of_b")
plt.close()
'''
