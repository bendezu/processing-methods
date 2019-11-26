import math

import numpy as np

from src.drawable.Drawable import Drawable


def window(drawable, alpha=0.46):
    return HammingWindow("Hamming Window", drawable, alpha)

class HammingWindow(Drawable):

    def __init__(self, title, drawable, alpha):
        self.drawable = drawable
        self.alpha = alpha
        super(HammingWindow, self).__init__(title, drawable.getN())

    def calculateY(self):
        result = [0] * self.getN()
        for i in range(self.getN()):
            result[i] = self.drawable.y[i] * (self.alpha - (1 - self.alpha) * math.cos(2 * math.pi * self.x[i] / self.getN()))
        return np.array(result)