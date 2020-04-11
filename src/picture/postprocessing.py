import copy
import math
import numpy as np

from src.line.Line import Line
from src.picture.Picture import Picture
from src.transform.convolution import _deconv, _regularized_deconv


def neg(picture, clone=True):
    pic = copy.deepcopy(picture) if clone else picture
    l_max = 255
    for pixel in np.nditer(pic.matrix, op_flags=['readwrite']):
        pixel[...] = l_max - pixel
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

def transform(picture, function, clone=True):
    pic = copy.deepcopy(picture) if clone else picture
    for pixel in np.nditer(pic.matrix, op_flags=['readwrite']):
        pixel[...] = function.y[pixel]
    return pic

def deconv_pic(picture: Picture, kernel: Line, clone=True):
    pic = copy.deepcopy(picture) if clone else picture
    rows, cols = picture.matrix.shape
    for i in range(rows):
        row = picture.matrix[i]
        pic.matrix[i] = _deconv(row, kernel.y)
    return pic

def reg_deconv_pic(picture: Picture, kernel: Line, k, clone=True):
    pic = copy.deepcopy(picture) if clone else picture
    rows, cols = picture.matrix.shape
    for i in range(rows):
        row = picture.matrix[i]
        pic.matrix[i] = _regularized_deconv(row, kernel.y, k)
    return pic
