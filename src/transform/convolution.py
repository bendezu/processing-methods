import numpy as np

from src.drawable.Drawable import Drawable
from src.util.common import N

def conv(d1, d2):
    return Convolution("Conv of " + d1.title + " and " + d2.title, d1, d2)

class Convolution(Drawable):

    def __init__(self, title, drawable_first, drawable_second):
        self.drawable_first = drawable_first
        self.drawable_second = drawable_second
        super(Convolution, self).__init__(title, drawable_first.getN())

    def calculateY(self):
        n = self.drawable_first.getN()
        m = self.drawable_second.getN()
        result = np.zeros(n)
        for i in range(n):
            summ = 0
            if 0 <= i < n + m - 1:
                for j in range(m):
                    if 1 <= i - j < n:
                        summ += self.drawable_first.y[i - j] * self.drawable_second.y[j]
            result[i] = summ
        return result
