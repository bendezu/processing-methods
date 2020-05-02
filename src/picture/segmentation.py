import copy

import cv2
import numpy as np

from scipy import ndimage
from src.picture.Picture import Picture
from src.util.common import DEF_MORTH_SIZE


def thresholding(picture: Picture, thresh=100, clone=True):
    pic = copy.deepcopy(picture) if clone else picture
    _, pic.matrix = cv2.threshold(picture.matrix, thresh, 255, cv2.THRESH_BINARY)
    return pic

def diff_pic(picture: Picture, axis='full', clone=True):
    pic = copy.deepcopy(picture) if clone else picture
    dy = np.diff(picture.matrix.astype('int32'), axis=0, append=0)
    dx = np.diff(picture.matrix.astype('int32'), axis=1, append=0)
    if axis == 'full':
        pic.matrix = np.hypot(dx, dy)
    elif axis == 'x':
        pic.matrix = np.abs(dx)
    elif axis == 'y':
        pic.matrix = np.abs(dy)
    return pic

def sobel(picture: Picture, axis='full', clone=True):
    pic = copy.deepcopy(picture) if clone else picture
    sy = ndimage.sobel(picture.matrix.astype('int'), axis=0, mode='constant')
    sx = ndimage.sobel(picture.matrix.astype('int'), axis=1, mode='constant')
    if axis == 'full':
        pic.matrix = np.hypot(sx, sy)
    elif axis == 'x':
        pic.matrix = np.abs(sx)
    elif axis == 'y':
        pic.matrix = np.abs(sy)
    return pic

def laplace(picture: Picture, axis='full', clone=True):
    pic = copy.deepcopy(picture) if clone else picture
    # dy = np.diff(picture.matrix.astype('int32'), n=2, axis=0, append=np.zeros((2, 400)))
    # dx = np.diff(picture.matrix.astype('int32'), n=2, axis=1, append=np.zeros((300, 2)))
    # if axis == 'full':
    #     pic.matrix = dx + dy
    # elif axis == 'x':
    #     pic.matrix = dx
    # elif axis == 'y':
    #     pic.matrix = dy
    ndimage.filters.laplace(picture.matrix, pic.matrix)
    return pic

def erode(picture: Picture, size=DEF_MORTH_SIZE, clone=True):
    pic = copy.deepcopy(picture) if clone else picture
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))
    pic.matrix = cv2.erode(picture.matrix, kernel)
    return pic

def dilate(picture: Picture, size=DEF_MORTH_SIZE, clone=True):
    pic = copy.deepcopy(picture) if clone else picture
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))
    pic.matrix = cv2.dilate(picture.matrix, kernel)
    return pic

def opening(picture: Picture, size=DEF_MORTH_SIZE, clone=True):
    # erosion followed by dilation
    pic = copy.deepcopy(picture) if clone else picture
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))
    pic.matrix = cv2.morphologyEx(picture.matrix, cv2.MORPH_OPEN, kernel)
    return pic

def closing(picture: Picture, size=DEF_MORTH_SIZE, clone=True):
    # dilation followed by erosion
    pic = copy.deepcopy(picture) if clone else picture
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))
    pic.matrix = cv2.morphologyEx(picture.matrix, cv2.MORPH_CLOSE, kernel)
    return pic
