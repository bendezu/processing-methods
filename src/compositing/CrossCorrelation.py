import numpy as np

from src.drawable.Drawable import Drawable
from src.util.common import N


class CrossCorrelation(Drawable):

    def __init__(self, title, drawable_first, drawable_second, start=0, end=N):
        self.drawable_first = drawable_first
        self.drawable_second = drawable_second
        self.start = start
        self.end = end
        super(CrossCorrelation, self).__init__(title,drawable_first.getN())

    def calculateY(self):
        mean_first = self.drawable_first.getMean(self.drawable_first.y)
        mean_second = self.drawable_second.getMean(self.drawable_second.y)
        result = [0.0] * self.end
        divider = 0
        for k in range(self.start,self.end):
            divider += ((self.drawable_first.y[k] - mean_first) ** 2) *\
                       ((self.drawable_second.y[k] - mean_second) ** 2)
        divider = np.sqrt(divider)

        for funShift in range(self.start, self.end):
            temp = 0
            for k in range(0, self.end - funShift):
                temp += (self.drawable_first.y[k] - mean_first) * (self.drawable_second.y[k + funShift] - mean_second)
            temp /= divider
            result[funShift - self.start] = temp
        return result
