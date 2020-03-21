import copy
import random

import numpy as np
from src.picture.Picture import Picture


def gaussian_noise(picture: Picture, percent, clone=True):
    pic = copy.deepcopy(picture) if clone else picture
    mean = 0
    var = percent * 255
    sigma = var ** 0.5
    rows, cols = picture.matrix.shape
    gauss = np.random.normal(mean, sigma, (rows, cols)).reshape(rows, cols)
    pic.matrix = picture.matrix + gauss.astype(np.uint8)
    return pic

def salt_and_pepper(picture: Picture, percent=0.05, clone=True):
    pic = copy.deepcopy(picture) if clone else picture
    for pixel in np.nditer(pic.matrix, op_flags=['readwrite']):
        if random.random() < percent:
            salt_or_pepper = random.choice([0, 255])
            pixel[...] = salt_or_pepper
    return pic

def all_noise(picture: Picture, gaus_percent, snp_percent, clone=True):
    return salt_and_pepper(gaussian_noise(picture, gaus_percent, clone), snp_percent, clone=False)
