import numpy as np
from collections import deque


def neighbour(i):
    global Lbig
    ix, iy = i
    return [(ix, (iy+1) % Lbig), (ix, (iy-1) % Lbig),
            ((ix+1) % Lbig, iy), ((ix-1) % Lbig, iy)]


def update(i):
    global s, heff
    s[i] = 1
    for j in neighbour(i):
        heff[j] += 2.
    return


def toScreen(a):
    print(a)
    global x
    print(x)
