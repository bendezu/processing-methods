import copy
import random

import numpy as np
from src.picture.Picture import Picture


def gaussian_noise(picture: Picture, percent, clone=True):
    pic = copy.deepcopy(picture) if clone else picture
    mean = 0
    std_dev = 255 / 2 * percent
    rows, cols = picture.matrix.shape
    gauss = np.random.normal(mean, std_dev, (rows, cols)).reshape(rows, cols)
    pic.matrix = (picture.matrix + gauss).astype('uint8')
    return pic

def salt_and_pepper(picture: Picture, percent, clone=True):
    pic = copy.deepcopy(picture) if clone else picture
    for pixel in np.nditer(pic.matrix, op_flags=['readwrite']):
        if random.random() < percent:
            salt_or_pepper = random.choice([0, 255])
            pixel[...] = salt_or_pepper
    return pic

def all_noise(picture: Picture, gaus_percent, snp_percent, clone=True):
    return salt_and_pepper(gaussian_noise(picture, gaus_percent, clone), snp_percent, clone=False)
