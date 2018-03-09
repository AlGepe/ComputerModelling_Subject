import numpy as np
import matplotlib.pyplot as plt
import Figures
# Game of Life implemente in python

# Rules are expressed as (Survival/Birth)
# Game of Life:


def calculateNeighbours(grid):
    neighbours = np.zeros(grid.shape)
    neighbours[1:-1, 1:-1] += grid[0:-2, 0:-2] + grid[0:-2, 1:-1] \
        + grid[0:-2, 2:] + grid[1:-1, 0:-2] + grid[1:-1, 2:] \
        + grid[2:, 0:-2] + grid[2:, 1:-1] + grid[2:, 2:]

    return neighbours


def updateUniverse(state, neighbours):
    birth = np.zeros(state.shape)
    # birth += (neighbours == 3) & (state == 0) * 1
    # birth += (neighbours == 2) & (state == 0) * 1
    birth += (neighbours == 4) & (state == 0) * 1
    birth += (neighbours == 5) & (state == 0) * 1
    birth += (neighbours == 6) & (state == 0) * 1
    birth += (neighbours == 7) & (state == 0) * 1
    birth += (neighbours == 8) & (state == 0) * 1
    survival = np.zeros(state.shape)
    # survival += (neighbours == 1) * 1
    survival += (neighbours == 2) * 1
    survival += (neighbours == 3) * 1
    survival += (neighbours == 4) * 1
    survival += (neighbours == 5) * 1
    # survival += (neighbours == 6) * 1
    # survival += (neighbours == 7) * 1
    # survival += (neighbours == 8) * 1
    newUniverse = birth + (survival * state)

    return newUniverse


universe = np.zeros((256, 512))
universe[125:131, 253:259] += Figures.randSquare(6)
universe = Figures.radomUniverse()
# universe[200-len(figure):200, 406:406+len(figure[0])] += figure # blinker
# figure = Figures.oneOone()
# universe[100-len(figure):100, 156:156+len(figure[0])] += figure
steps = 500
for i in range(0, steps):
    plt.imshow(universe, interpolation='nearest', cmap=plt.cm.gray_r)
    plt.axis('off')
    neighbours = calculateNeighbours(universe)
    universe = updateUniverse(universe, neighbours)
    filename = './png/otherLifeWalled/' + 'GoL' + str(i) + '.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.clf()
