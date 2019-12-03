import numpy as np

from src.drawable.Drawable import Drawable
from src.filter.halflowpass import half_low_pass_filter
from src.filter.lowpass import low_pass_filter
from src.util.common import N

def highpass(n=128, dt=0.001, fCut=50):
    return Drawable("High Pass Filter", y=high_pass_filter(n, dt, fCut))

def high_pass_filter(n, dt, fCut):
    result = low_pass_filter(n, dt, fCut)
    for i in range(len(result)):
        if i == n:
            result[i] = 1 - result[i]
        else:
            result[i] = -result[i]
    return result
