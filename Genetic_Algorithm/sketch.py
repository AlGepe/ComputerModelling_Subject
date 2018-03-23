import numpy as np
from functions import calculateNeighbours, newGeneration, gradeResult

genPopulation = 20
gridSize = 20

flock = np.random.randint(2, size=(genPopulation, 512))
grades = np.zeros(genPopulation)
bestGrade = 0
threshold = 10 * gridSize * gridSize

while (bestGrade < threshold):  # While not good enough
    for justOne in range(0, genPopulation):  # for all individuals
        phenotype = flock[justOne]
        worldGrid = np.random.randint(2, size=(gridSize, gridSize))
        for i in range(0, 100):  # time evol all the worlds
            neighboursGrid = calculateNeighbours(worldGrid)
            size = neighboursGrid.shape
            for x in range(0, size[0]):
                for y in range(0, size[1]):
                    print(type(neighboursGrid[x][y]))
                    worldGrid[x][y] = phenotype[neighboursGrid[x][y]]

        grades[justOne] = gradeResult(worldGrid)  # Grade this individual

bestGrade = max(grades)

print("done")

# While fit is not good enough

    # Create new generation

    # evolve in time

    # grade Rules




