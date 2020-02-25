import numpy as np

from src.line.Line import Line


def histogram(picture):
    hist = np.zeros(256)
    for pixel in np.nditer(picture.matrix, op_flags=['readwrite']):
        hist[pixel] += 1
    return Line('histogram of ' + picture.title, y=hist)

# Cumulative distribution function
def cdf(picture, normalise=True):
    hist = np.array(histogram(picture).y)
    for i in range(1, hist.size):
        hist[i] += hist[i - 1]
    if normalise:
        m = hist.max()
        for i in range(1, hist.size):
            hist[i] = int(hist[i] / m * 255)
    return Line('CDF of ' + picture.title, y=hist)
