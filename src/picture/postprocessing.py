import copy
import math

import numpy as np


def neg(picture, clone=True):
    pic = copy.deepcopy(picture) if clone else picture
    l_max = 255
    for pixel in np.nditer(pic.matrix, op_flags=['readwrite']):
        pixel[...] = l_max - pixel

    # rows, cols = matrix.shape
    # for i in range(rows):
    #     for j in range(cols):
    #         matrix[i, j] = l_max - matrix[i,j]
    return pic

def gamma(picture, C, gamma, clone=True):
    pic = copy.deepcopy(picture) if clone else picture
    for pixel in np.nditer(pic.matrix, op_flags=['readwrite']):
        pixel[...] = C * pixel ** gamma
    return pic

def log(picture, C, clone=True):
    pic = copy.deepcopy(picture) if clone else picture
    for pixel in np.nditer(pic.matrix, op_flags=['readwrite']):
        pixel[...] = C * math.log(pixel + 1)
    return pic