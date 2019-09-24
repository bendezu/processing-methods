import numpy as np
from src.drawable.Drawable import Drawable


class Exp(Drawable):

    def __init__(self, title, N, alpha, beta):
        self.alpha = alpha
        self.beta = beta
        super(Exp, self).__init__(title, N)

    def calculateY(self):
        return self.beta * np.exp(self.alpha * self.x)
