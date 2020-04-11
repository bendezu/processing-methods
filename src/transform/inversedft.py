import math
import numpy as np

from src.line.Line import Line
from src.transform.fouriertransform import _dft

def idft(drawable):
    return InverseDiscreteFourierTransform("Inverse DFT", drawable)

class InverseDiscreteFourierTransform(Line):

    def __init__(self, title, drawable):
        self.drawable = drawable
        super(InverseDiscreteFourierTransform, self).__init__(title, drawable.getN())

    def calculateY(self):
        reals, imags = _dft(self.drawable.y)
        return _idft(reals, imags)

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