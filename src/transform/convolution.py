import math
import numpy as np

from src.line.Line import Line

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

def deconv(d1, d2):

    def _idft(reals, imags):
        n = len(reals)
        result = np.zeros(n)
        for k in range(n):
            summ = 0
            for t in range(n):
                angle = (2 * math.pi * k * t) / n
                summ += reals[t] * math.cos(angle) + imags[t] * math.sin(angle)
            result[k] = summ
        return result

    def _dft(y):
        n = len(y)
        reals = np.zeros(n)
        imags = np.zeros(n)
        for k in range(n):
            sumReal = 0
            sumImag = 0
            for t in range(n):
                angle = (2 * math.pi * k * t) / n
                sumReal += y[t] * math.cos(angle)
                sumImag += y[t] * math.sin(angle)
            reals[k] = sumReal / n
            imags[k] = sumImag / n
        return reals, imags

    r_1, i_1 = _dft(d1.y)
    r_2, i_2 = _dft(d2.y)
    r_3 = np.zeros(len(r_1))
    i_3 = np.zeros(len(r_1))

    for i in range(len(r_3)):
        a = r_1[i]
        b = i_1[i]
        c = r_2[i]
        d = i_2[i]
        r_3[i] = (a * c + b * d) / (c * c + d * d)
        i_3[i] = (b * c - a * d) / (c * c + d * d)

    return Line("Deconv of " + d1.title + " and " + d2.title, y=_idft(r_3, i_3))
