import copy

import numpy as np
from scipy import signal

from src.line.Line import Line
from src.filter.halflowpass import half_low_pass_filter
from src.picture.Picture import Picture
from src.util.common import N

def lowpass(n=128, dt=0.001, fCut=50):
    return Line("Low Pass Filter", y=low_pass_filter(n, dt, fCut))

def low_pass_filter(n, dt, fCut):
    second_half = half_low_pass_filter(n, dt, fCut)
    first_half = np.flip(np.copy(second_half))
    return np.concatenate([first_half, second_half[1:]])

def lpf_line(line: Line, cut):
    y = _lpf(line.y, cut, fs=len(line.y))
    return Line(title="lpf of " + line.title, y=y)

def lpf_pic(picture: Picture, cut, clone=True):
    pic = copy.deepcopy(picture) if clone else picture
    rows, cols = picture.matrix.shape
    for i in range(rows):
        row = picture.matrix[i]
        pic.matrix[i] = _lpf(row, cut, len(row))
    return pic

def _lpf(data, cut, fs, order=1):
    nyq = 0.5 * fs
    f_cut = cut / nyq
    b, a = signal.butter(order, f_cut, btype='low')
    return signal.lfilter(b, a, data)
