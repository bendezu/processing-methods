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

    def suppress_spikes(self, min_y, max_y):
        for i in range(self.getN()):
            if self.y[i] < min_y or self.y[i] > max_y:
                self.y[i] = (self.y[i-1] + self.y[i+1]) / 2

    def anti_trend(self, window_size=3):
        window_radius = int(window_size / 2)
        means = [0] * self.getN()
        for i in range(self.getN()):
            window_start = max(i - window_radius, 0)
            window_end = min(i + window_radius, self.getN())
            means[i] = self.getMean(self.y[window_start:window_end])
        for i in range(self.getN()):
            self.y[i] = self.y[i] - means[i]


    def shift(self, offset, start=0, end=None):
        end = self.getN() if end is None else end
        for pos in range(start, end):
            self.y[int(pos)] = self.y[int(pos)] + offset

    def anti_shift(self):
        mean = self.getMean(self.y)
        self.shift(-mean)

    def is_stationary(self, intervals, delta_percent):
        delta = (np.max(self.y) - np.min(self.y)) * delta_percent
        interval_size = int(len(self.x) / intervals)
        means = [None] * intervals
        dispersions = [None] * intervals

        for interval in range(0, intervals):
            start = interval * interval_size
            end = start + interval_size
            means[interval] = self.getMean(self.y[start:end])
            dispersions[interval] = self.getDispersion(self.y[start:end])

        # print("Среднее[] :" + str(means))
        # print("Дисперсия[] " + str(dispersions))

        for i in range(0, intervals - 1):
            if (math.sqrt(abs(dispersions[i] - dispersions[i + 1])) > delta * 2) or (abs(means[i] - means[i + 1]) > delta):
                return False
        return True

    def getMean(self, array):
        return sum(array) / len(array)

    def getDispersion(self, array):
        return self.m(power=2, array=array)

    def getStdDev(self, array=None):
        array = self.y if array is None else array
        return math.sqrt(self.getDispersion(array))

    def m(self, power, array=None):
        array = self.y if array is None else array
        mean = self.getMean(array)
        return sum((xi - mean) ** power for xi in array) / len(array)

    def absDev(self, array=None):
        array = self.y if array is None else array
        mean = self.getMean(array)
        return sum(abs(xi - mean) for xi in array) / len(array)

    def gamma1(self):
        return self.m(power=3) / (self.getStdDev() ** 3)

    def gamma2(self):
        return self.m(power=4) / (self.getStdDev() ** 4) - 3

    def psi2(self):
        return sum(xi ** 2 for xi in self.y) / len(self.y)

    def epsilon(self):
        return math.sqrt(self.psi2())

    def getN(self):
        return len(self.x)

    def calculateY(self):
        pass
