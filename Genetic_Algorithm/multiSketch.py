import time
import numpy as np
import multiprocessing
import matplotlib
from functools import partial
from functions import newGeneration, getFitFunction
matplotlib.use('pdf')
import matplotlib.pyplot as plt

# genPopulation = 100
# gridSize = 10
iterations = 1000
t_0 = time.time()
jVector = np.linspace(1, 20, num=3)
hVector = np.linspace(1, 20, num=3)

for j in jVector:
    for h in hVector:
        for k in range(0, 2):
            gridSize = int(j * 10)
            genPopulation = int(h * 10)
            flock = np.random.randint(2, size=(genPopulation, 512))
            grades = np.zeros(genPopulation)
            bestGrade = 0
            threshold = 8.5 * gridSize * gridSize
            plotGrades = np.zeros(iterations)
            allGrids = np.ndarray(10, dtype=object)
            i = 0
            num_cores = int(multiprocessing.cpu_count())

            while (bestGrade < threshold) and (i < iterations):
                # While not good enough
                # print(grades)
                flock = newGeneration(flock, grades)
                for j in range(0, 10):
                    allGrids[j] = np.random.randint(2,
                                                    size=(gridSize, gridSize))
                with multiprocessing.Pool(processes=num_cores) as pool:
                    for ind in range(0, genPopulation):  # for all individuals
                        # phenotype = flock[ind]
                        get_phenotypeFF = partial(getFitFunction,
                                                  individual=flock[ind])
                        grades_of_phenotype = pool.map(get_phenotypeFF,
                                                       allGrids)
                        grades[ind] = sum(grades_of_phenotype)/10.

                bestGrade = max(grades)
                for m in range(0, genPopulation):
                    if grades[m] == bestGrade:
                        fileQuick = open('Best.txt', 'w')
                        fileQuick.write(str(flock[m]))
                plotGrades[i] = bestGrade

                i += 1
                if i % 100 == 0:
                    print("Iteration: " + str(i))
                    print("For Population: " + str(genPopulation) +
                          " and gridsize: " + str(gridSize))
                    print(str((bestGrade / threshold) * 100) + '%')
                    print(t_0)
                    t1 = time.time()
                    print("\n Time: " + str(t1-t_0))
                    t_0 = time.time()

            print("solved One of them")
            for m in range(0, genPopulation):
                if grades[m] == bestGrade:
                    fileQuick = open('Best.txt', 'w')
                    fileQuick.write(str(flock[m]))

            iterVector = np.linspace(1, i, i)
            plt.close()
            plt.plot(iterVector, plotGrades[:i])
            finishStatement = "FF_Grid" + str(gridSize) + "_popSize" +  \
                str(genPopulation) + "_iter" + str(i) + "_99perc_" + str(k) \
                + ".png"
            plt.savefig(finishStatement, dpi=300, bbox_inches='tight')
            # plt.show()
print("done")
