import math
import random

import numpy as np


class Drawable:

    def __init__(self, title, N=0, x=None, y=None):
        self.title = title
        self.x = x if N == 0 else np.arange(0, N, 1)
        self.y = self.calculateY() if y is None else y

    def normalize(self, S):
        norm_x = ((self.x - self.x.min()) / (self.x.max() - self.x.min()) - 0.5) * 2 * S
        self.x = norm_x

    def add_spikes(self, count, size_multiplier):
        positions = np.random.uniform(low=0, high=len(self.x), size=count, )
        y_range = (np.max(self.y) - np.min(self.y))
        for pos in positions:
            sign = 1 if random.random() < 0.5 else -1
            self.y[int(pos)] = self.y[int(pos)] + y_range * size_multiplier * random.random() * sign

    def shift(self, start, end, offset):
        for pos in range(start, end):
            self.y[int(pos)] = self.y[int(pos)] + offset

    def isStationar(self, intervals, delta_percent):
        delta = (np.max(self.y) - np.min(self.y)) * delta_percent
        interval_size = int(len(self.x) / intervals)
        means = [None] * intervals
        dispersions = [None] * intervals

        for interval in range(0, intervals):
            start = interval * interval_size
            end = start + interval_size
            means[interval] = self.getMean(self.y[start:end])
            dispersions[interval] = self.getDispersion(self.y[start:end])

        for i in range(0, intervals):
            for j in range(i, intervals):
                if (abs(dispersions[i] - dispersions[j]) > delta) or (abs(means[i] - means[j]) > delta):
                    return False
        return True

    def getMean(self, array):
        return sum(array) / len(array)

    def getDispersion(self, array):
        mean = self.getMean(array)
        return sum((xi - mean) ** 2 for xi in array) / len(array)

    def getStdDev(self, array = None):
        array = self.y if array is None else array
        return math.sqrt(self.getDispersion(array))

    def getN(self):
        return len(self.x)

    def calculateY(self):
        pass
