import copy
import numpy as np
import math


def newGeneration(genPopulation):
    return np.random.randint(2, size=(genPopulation, 512))


def newGeneration(prevGeneration, grades):
    # Create rules
    cutOff = np.median(grades)
    newGeneration = np.zeros(shape=(prevGeneration.shape))
    valid = []
    for i in range(0, len(grades)):  # find useful
        if (grades[i] >= cutOff):  # Keep
            valid.append(i)
            validPerm = copy.deepcopy(valid)
    for i in range(0, len(newGeneration)):  # find useful
        if valid :
            newGeneration[i] = reproduce(prevGeneration[valid.pop()], \
                                         prevGeneration[valid.pop()])
        else:
            randIndex = np.random.randint(len(valiPerm))
            newGeneration = mutate(valiPerm[randIndex])

    return newGeneration


def reproduce(father, mother):
    sizeParents = len(mother)
    child = mother
    for i in range(0, sizeParents):
        f_m = np.random.randint(2)
        if f_m :
            child[i] = father[i]
    return child


def mutate(individual):
    for i in range(0, len(individual)):
        if np.random.uniform(0, 1) > 0.8:
            individual[i] = np.random.randint(2)
    return individual

def nextTimeEvolution(worldGrid, rule):
    neighboursGrid = calculateNeighbours(worldGrid)
    size = neighboursGrid.shape
    for i in range(0, size[0]):
        for j in range(0, size[1]):
            newWorld = rule[neighboursGrid[i][j]]

    return newWorld


def gradeResult(worldGrid):
    grade = np.zeros(worldGrid.shape)
    firstCheck = (worldGrid == np.roll(worldGrid, 1, axis=0)) or  \
                 (worldGrid == np.roll(worldGrid, 1, axis=1))
    secondCheck = worldGrid == np.roll(worldGrid, [1, 1], axis=[0, 1])
    thirdCheck = worldGrid == np.roll(worldGrid, [1, -1], axis=[0, 1])
    grade = firstCheck * -3
    # Positive diagonal points
    grade += ((not firstCheck) * (8 * secondCheck + thirdCheck))
    grade -= ((not firstCheck) * (5 * (not secondCheck) + (not thirdCheck)))

    # check for up or right neighbours
    return sum(sum(grade))

def calculateNeighbours(worldGrid):
    neighbours = math.pow(2, 0) * np.roll(worldGrid, [1, 1], axis=[0, 1]) + \
                 math.pow(2, 1) * np.roll(worldGrid, [1, 0], axis=[0, 1]) + \
                 math.pow(2, 2) * np.roll(worldGrid, [1, -1], axis=[0, 1]) + \
                 math.pow(2, 3) * np.roll(worldGrid, [0, 1], axis=[0, 1]) + \
                 math.pow(2, 4) * np.roll(worldGrid, [0, 0], axis=[0, 1]) + \
                 math.pow(2, 5) * np.roll(worldGrid, [0, -1], axis=[0, 1]) + \
                 math.pow(2, 6) * np.roll(worldGrid, [-1, 1], axis=[0, 1]) + \
                 math.pow(2, 7) * np.roll(worldGrid, [-1, 0], axis=[0, 1]) + \
                 math.pow(2, 8) * np.roll(worldGrid, [-1, -1], axis=[0, 1])

    return neighbours
