import copy

import cv2
import numpy as np

from scipy import ndimage
from src.picture.Picture import Picture


def thresholding(picture: Picture, thresh=100, clone=True):
    pic = copy.deepcopy(picture) if clone else picture
    _, pic.matrix = cv2.threshold(picture.matrix, thresh, 255, cv2.THRESH_BINARY)
    return pic

def sobel(picture: Picture, clone=True):
    pic = copy.deepcopy(picture) if clone else picture
    sx = ndimage.sobel(picture.matrix.astype('int'), axis=0, mode='constant')
    sy = ndimage.sobel(picture.matrix.astype('int'), axis=1, mode='constant')
    pic.matrix = np.hypot(sx, sy)
    return pic


