import math
# time_step
def doStep(p0, x0):
    p1 = p0 + koupling*math.sin(x0)
    x1 = x0 + p1
    return p1, x1

