import math

import numpy as np
from src.drawable.Drawable import Drawable
from src.util.common import N

def halflowpass(n=128, dt=0.001, fCut=50):
    return Drawable("Half Low Pass Filter", y=half_low_pass_filter(n, dt, fCut))

SMOOTH_WINDOW_P310 = [0.35577019, 0.24369830, 0.07211497, 0.00630165]

def half_low_pass_filter(n, dt, fCut):
    result = np.zeros(n + 1)
    param = 2 * dt * fCut
    result[0] = param
    param *= math.pi
    for i in range(1, n + 1):
        result[i] = math.sin(param * i) / (math.pi * i)

    result[n] /= 2

    sumg = result[0]
    for i in range(1, n + 1):
        sum = SMOOTH_WINDOW_P310[0]
        arg = (math.pi * i) / n
        for k in range(1, 4):
            sum += 2 * SMOOTH_WINDOW_P310[k] * math.cos(arg * k)
        result[i] *= sum
        sumg += result[i] * 2

    for i in range(n + 1):
        result[i] /= sumg

    return result
