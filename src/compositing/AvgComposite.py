import numpy as np

from src.drawable.Drawable import Drawable


class AvgComposite(Drawable):

    def __init__(self, title, drawable, *args):
        self.drawable = drawable
        self.args = args
        super(AvgComposite, self).__init__(title, drawable.getN())

    def calculateY(self):
        result = self.drawable.y
        for arg in self.args:
            result = result + arg.y
        return result / len(self.args)
