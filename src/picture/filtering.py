import copy

from scipy import signal

import numpy as np
from src.picture.Picture import Picture

def mean_filter(picture: Picture, size=5):
    matrix = __base_filter(picture.matrix, size, lambda window: np.average(window))
    return Picture(picture.title, matrix)

def median_filter(picture: Picture, size=5):
    matrix = signal.medfilt2d(picture.matrix, kernel_size=size)  # a lot faster
    # matrix = __base_filter(picture.matrix, window_size, lambda window: np.median(window))
    return Picture(picture.title, matrix)

def __base_filter(nparray, window_size, on_apply_window):
    radius = int(window_size / 2)
    matrix = copy.deepcopy(nparray)
    rows, cols = matrix.shape
    for i in range(radius, rows - radius):
        for j in range(radius, cols - radius):
            window = []
            for i_window in range(i - radius, i + radius):
                for j_window in range(j - radius, j + radius):
                    window.append(nparray[i_window, j_window])
            matrix[i, j] = on_apply_window(window)
    return matrix
