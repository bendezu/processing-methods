import math
import numpy as np

from src.picture.Picture import Picture


def _nearest_neighbor(picture, h_target, w_target, h_ratio, w_ratio, target):
    for i in range(h_target):
        for j in range(w_target):
            pw = math.floor(j / w_ratio)
            ph = math.floor(i / h_ratio)
            target[i, j] = picture.matrix[ph, pw]

def scale(picture, ratio=None, w_ratio=None, h_ratio=None, w_target=None, h_target=None, strategy="nearest-neighbor"):
    h, w = picture.matrix.shape
    if ratio is not None:
        w_ratio = ratio
        h_ratio = ratio
        w_target = round(w * w_ratio)
        h_target = round(h * h_ratio)
    elif w_ratio is not None:
        w_target = round(w * w_ratio)
        h_target = round(h * h_ratio)
    elif w_target is not None:
        w_ratio = w_target / w
        h_ratio = h_ratio / h
    scaled = np.empty((h_target, w_target))

    if strategy == "nearest-neighbor":
        _nearest_neighbor(picture, h_target, w_target, h_ratio, w_ratio, scaled)
    if strategy == "bilinear":
        pass

    ratio = (w_ratio + h_ratio) / 2 if ratio is None else ratio
    return Picture(picture.title + "(x"+str(ratio)+")", scaled)