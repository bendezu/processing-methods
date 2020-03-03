import math
import numpy as np

from src.picture.Picture import Picture


def _nearest_neighbor(picture, h_target, w_target, h_ratio, w_ratio, target):
    for i in range(h_target):
        for j in range(w_target):
            pw = math.floor(j / w_ratio)
            ph = math.floor(i / h_ratio)
            target[i, j] = picture.matrix[ph, pw]

# x=w, y=h
def _bilinear(picture, h_target, w_target, h_ratio, w_ratio, target):
    for i in range(h_target):
        for j in range(w_target):
            x = math.floor(j / w_ratio)
            y = math.floor(i / h_ratio)
            x_diff = (j / w_ratio) - x
            y_diff = (i / h_ratio) - y

            y_safe = y if y + 1 == picture.matrix.shape[0] else y + 1
            x_safe = x if x + 1 == picture.matrix.shape[1] else x + 1

            A = picture.matrix[y, x]
            B = picture.matrix[y, x_safe]
            C = picture.matrix[y_safe, x]
            D = picture.matrix[y_safe, x_safe]
            # // Y = A(1 - w)(1 - h) + B(w)(1 - h) + C(h)(1 - w) + Dwh
            gray = round(A * (1 - x_diff) * (1 - y_diff) + B * (x_diff) * (1 - y_diff) + C * (y_diff) * (1 - x_diff) + D * (x_diff * y_diff))
            target[i, j] = gray

def scale(picture, ratio=None, w_ratio=None, h_ratio=None, w_target=None, h_target=None, strategy="bilinear"):
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
        _bilinear(picture, h_target, w_target, h_ratio, w_ratio, scaled)

    ratio = (w_ratio + h_ratio) / 2 if ratio is None else ratio
    return Picture(picture.title + "(x"+str(ratio)+")", scaled)