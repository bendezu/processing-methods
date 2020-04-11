import math
import numpy as np

from src.line.Line import Line
from src.transform.fouriertransform import _dft
from src.transform.inversedft import _idft


def conv(d1, d2):
    return Convolution("Conv of " + d1.title + " and " + d2.title, d1, d2)

class Convolution(Line):

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

def deconv(d1: Line, d2: Line):
    return Line("Deconv of " + d1.title + " and " + d2.title, y=_deconv(d1.y, d2.y))

def _deconv(arr1, arr2):
    r_1, i_1 = _dft(arr1)
    r_2, i_2 = _dft(arr2)
    r_3, i_3 = _complex_division(r_1, i_1, r_2, i_2)
    return _idft(r_3, i_3)

def _complex_division(r1, i1, r2, i2):
    # (r1 + i i1) / (r2 + i i2)
    divider = (r2 ** 2 + i2 ** 2)
    r = (r1 * r2 + i1 * i2) / divider
    i = (i1 * r2 - r1 * i2) / divider
    return r, i
