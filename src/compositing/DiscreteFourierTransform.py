import math

from src.drawable.Drawable import Drawable


class DiscreteFourierTransform(Drawable):

    def __init__(self, title, drawable):
        self.drawable = drawable
        super(DiscreteFourierTransform, self).__init__(title, drawable.getN())

    def calculateY(self):
        n = self.getN()
        result = [0] * n
        for k in range(n):
            real_sum = 0
            imag_sum = 0
            for t in range(n):
                double_angle = 2 * math.pi * t * k / n
                real_sum += self.drawable.y[t] * math.cos(double_angle)
                imag_sum += self.drawable.y[t] * math.sin(double_angle)
            result[k] = math.sqrt(real_sum * real_sum + imag_sum * imag_sum)
        return  result