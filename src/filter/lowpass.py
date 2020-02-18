import numpy as np

from src.line.Line import Line
from src.filter.halflowpass import half_low_pass_filter
from src.util.common import N

def lowpass(n=128, dt=0.001, fCut=50):
    return Line("Low Pass Filter", y=low_pass_filter(n, dt, fCut))

def low_pass_filter(n, dt, fCut):
    second_half = half_low_pass_filter(n, dt, fCut)
    first_half = np.flip(np.copy(second_half))
    return np.concatenate([first_half, second_half[1:]])
