import math
import random
import numpy as np
from src.Plotable import Plotable

class Line(Plotable):

    def __init__(self, title, N=0, x=None, y=None):
        self.title = title
        length = N if y is None else len(y)
        self.x = np.arange(0, length, 1) if x is None else x
        self.y = self.calculateY() if y is None else y

    def get_title(self):
        return self.title

    def plot_on(self, subplot):
        subplot.plot(self.x, self.y)

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
                self.y[i] = (self.y[i - 1] + self.y[i + 1]) / 2

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

    def getMean(self, array=None):
        array = self.y if array is None else array
        return sum(array) / len(array)

    def getDispersion(self, array=None):
        array = self.y if array is None else array
        return self.m(power=2, array=array)

    def meanSquare(self, array=None):
        array = self.y if array is None else array
        return sum(array ** 2) / len(array)

    def getStdDev(self, array=None):
        return math.sqrt(self.getDispersion(array))

    def meanSquareDev(self, array=None):
        return math.sqrt(self.meanSquare(array))

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

    def maximum(self):
        return np.max(self.y)

    def minimum(self):
        return np.min(self.y)

    def getN(self):
        return len(self.x)

    def calculateY(self):
        pass
