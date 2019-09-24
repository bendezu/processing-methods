import numpy as np

from src.drawable.Drawable import Drawable


class AvgComposite(Drawable):

    def __init__(self, title, *args):
        self.args = args
        super(AvgComposite, self).__init__(title, args[0].getN())

    def calculateY(self):
        accum = np.zeros(len(self.args[0].x))
        for arg in self.args:
            accum = accum + arg.y
        return accum / len(self.args)
