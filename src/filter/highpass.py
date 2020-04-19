import copy

import numpy as np
from scipy import signal

from src.line.Line import Line
from src.filter.halflowpass import half_low_pass_filter
from src.filter.lowpass import low_pass_filter
from src.picture.Picture import Picture
from src.util.common import N

def highpass(n=128, dt=0.001, fCut=50):
    return Line("High Pass Filter", y=high_pass_filter(n, dt, fCut))

def high_pass_filter(n, dt, fCut):
    result = low_pass_filter(n, dt, fCut)
    for i in range(len(result)):
        if i == n:
            result[i] = 1 - result[i]
        else:
            result[i] = -result[i]
    return result

def hpf_line(line: Line, cut):
    y = _hpf(line.y, cut, fs=len(line.y))
    return Line(title="lpf of " + line.title, y=y)

def hpf_pic(picture: Picture, cut, clone=True):
    pic = copy.deepcopy(picture) if clone else picture
    rows, cols = picture.matrix.shape
    for i in range(rows):
        row = picture.matrix[i]
        pic.matrix[i] = _hpf(row, cut, len(row))
    return pic

def _hpf(data, cut, fs, order=1):
    nyq = 0.5 * fs
    f_cut = cut / nyq
    b, a = signal.butter(order, f_cut, btype='high')
    return signal.lfilter(b, a, data)

