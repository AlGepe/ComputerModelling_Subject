import time
import numpy as np
import multiprocessing
import matplotlib.pyplot as plt
from functools import partial
from functions import calculateNeighbours, newGeneration, \
                      getFitFunction, gradeResult

genPopulation = 10
gridSize = 10
iterations = 5000

flock = np.random.randint(2, size=(genPopulation, 512))
grades = np.zeros(genPopulation)
bestGrade = 0
threshold = 1 * gridSize * gridSize
plotGrades = np.zeros(iterations)
allGrids = np.ndarray(10, dtype=object)
i = 0
num_cores = multiprocessing.cpu_count()


while (bestGrade < threshold) and (i < iterations):  # While not good enough
    t0 = time.time()
    # print(grades)
    flock = newGeneration(flock, grades)
    for j in range(0, 10):
        allGrids[j] = np.random.randint(2, size=(gridSize, gridSize))
    with multiprocessing.Pool(processes=num_cores) as pool:
        for ind in range(0, genPopulation):  # for all individuals
            # phenotype = flock[ind]
            get_phenotypeFF = partial(getFitFunction, individual=flock[ind])
            grades_of_phenotype = pool.map(get_phenotypeFF, allGrids)
            grades[ind] = sum(grades_of_phenotype)/10.

    bestGrade = max(grades)
    plotGrades[i] = bestGrade

    # print("Time: " + str(time.time()-t0))
    i += 1
    if i % 50 == 0:
        print("Iteration: " + str(i))
        print(bestGrade)

iterVector = np.linspace(1, iterations, iterations)
plt.close()
plt.plot(iterVector, plotGrades)
plt.savefig("FF_500iter_test.png", dpi=300, bbox_inches='tight')
# plt.show()
print("done")
