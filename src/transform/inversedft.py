import math

from src.line.Line import Line

def idft(drawable):
    return InverseDiscreteFourierTransform("Inverse DFT", drawable)

class InverseDiscreteFourierTransform(Line):

    def __init__(self, title, drawable):
        self.drawable = drawable
        super(InverseDiscreteFourierTransform, self).__init__(title, drawable.getN())

    def calculateY(self):
        n = self.getN()
        reals, imags = self.dft()
        result = [0] * n
        for k in range(n):
            summ = 0
            for t in range(n):
                angle = (2 * math.pi * k * t) / n
                summ += reals[t] * math.cos(angle) + imags[t] * math.sin(angle)
            result[k] = summ
        return result

    def dft(self):
        n = self.getN()
        reals = [0] * n
        imags = [0] * n
        for k in range(n):
            sumReal = 0
            sumImag = 0
            for t in range(n):
                angle = (2 * math.pi * k * t) / n
                sumReal += self.drawable.y[t] * math.cos(angle)
                sumImag += self.drawable.y[t] * math.sin(angle)
            reals[k] = sumReal / n
            imags[k] = sumImag / n
        return reals, imags
