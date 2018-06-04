import numpy as np
from collections import deque

#============
# Functions
#============

def neighbour(i):
    global Lbig
    ix, iy = i
    neig = [(ix, (iy+1) % Lbig), (ix, (iy-1) % Lbig),
            ((ix+1) % Lbig, iy), ((ix-1) % Lbig, iy)]
    return neig


def update(i):
    global s, heff
    s[i] = 1
    for j in neighbour(i):
        heff[j] += 2.
    return


def shiftPB(original, shift):
    shifted = np.zeros(original.shape, dtype=type(original[0,0]))
    i = shift[0]
    j = shift[1]
    if j == 0 and i == 0:
        return original
    elif j == 0:
        shifted[i:, :] = original[:-i, :]
        shifted[:i, :] = original[-i:, :]

    elif i == 0:
        shifted[:, j:] = original[:, :-j]
        shifted[:, :j] = original[:, -j:]

    else:
        # Big Square (for big N and small shifts)
        shifted[i:, j:] = original[:-i, :-j]
        # Small Square (for big N and small shifts)
        shifted[:i, :j] = original[-i:, -j:]
        # 'Bottom slice' for positive i and j
        shifted[:i, j:] = original[-i:, :-j]
        # 'Right slide' (for positive i and j)
        shifted[i:, :j] = original[:-i, -j:]
    return shifted


#==========
#   Code
#==========
flipCandidates = deque()
r_list = [0.7, 0.9, 1.4]
# for R in r_list
R = r_list[0]
N = 100
h = np.random.normal(0., R, size=(N, N))
s = np.full(shape=(N, N), fill_value=-1.)
H_t = 0

heff = (shiftPB(s, [-1, 1]) + shiftPB(s, [0, 1]) + shiftPB(s, [1, 1]) +
        shiftPB(s, [-1, -1]) + shiftPB(s, [0, -1]) + shiftPB(s, [1, -1]) +
        shiftPB(s, [-1, 0]) + shiftPB(s, [1, 0])) + H_t + h


itrig = np.unravel_index(np.argmax(heff + (s+1) * (-100)), h.shape)
flipCandidates.append(itrig)

# while s.any(-1):
while not(flipCandidates.empty()):
    i = flipCandidates.popleft()
    H_t -= (heff[i]) # checked (sets H_t to -internal field)
    update(i)
    flipCandidates.append([i[0] + 1, i[1] - 1])
    flipCandidates.append([i[0] + 1, i[1]    ])
    flipCandidates.append([i[0] + 1, i[1] + 1])
    flipCandidates.append([i[0]    , i[1] - 1])
    flipCandidates.append([i[0]    , i[1] + 1])
    flipCandidates.append([i[0] - 1, i[1] - 1])
    flipCandidates.append([i[0] - 1, i[1]    ])
    flipCandidates.append([i[0] - 1, i[1] + 1])
    # if spin not flipped
        # flip spin
    # update local fields
    # append all unflipped neighbours with positive local fields 


flipCandidates.append([itrig[0] + 1, itrig[1] - 1])
flipCandidates.append([itrig[0] + 1, itrig[1]    ])
flipCandidates.append([itrig[0] + 1, itrig[1] + 1])
flipCandidates.append([itrig[0]    , itrig[1] - 1])
flipCandidates.append([itrig[0]    , itrig[1] + 1])
flipCandidates.append([itrig[0] - 1, itrig[1] - 1])
flipCandidates.append([itrig[0] - 1, itrig[1]    ])
flipCandidates.append([itrig[0] - 1, itrig[1] + 1])
H_t -= -(heff[itrig])

