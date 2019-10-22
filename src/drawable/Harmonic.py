import math

from src.drawable.Drawable import Drawable

import numpy as np


class Harmonic(Drawable):

    def __init__(self, title, N, A0, f0, delta_t):
        self.A0 = A0
        self.f0 = f0
        self.delta_t = delta_t
        super(Harmonic, self).__init__(title, N)

    def calculateY(self):
        return np.array([self.A0 * math.sin(2 * math.pi * self.f0 * xi * self.delta_t) for xi in self.x])
