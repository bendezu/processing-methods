import numpy as np
from src.drawable.Drawable import Drawable


class Random(Drawable):

    def __init__(self, title, N, fromNum, toNum):
        self.fromNum = fromNum
        self.toNum = toNum
        super(Random, self).__init__(title, N)

    def calculateY(self):
        return np.random.uniform(low=self.fromNum, high=self.toNum, size=(len(self.x),))
