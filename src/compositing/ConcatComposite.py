import numpy as np

from src.drawable.Drawable import Drawable


class ConcatComposite(Drawable):

    def __init__(self, title, drawable, *args):
        self.drawable = drawable
        self.args = args
        n = drawable.getN()
        for arg in args:
            n += arg.getN()
        super(ConcatComposite, self).__init__(title, n)

    def calculateY(self):
        result = self.drawable.y
        for arg in self.args:
            left = result[-1]
            right = arg.y[0]
            arg.shift(offset=left - right)
            result = np.concatenate((result, arg.y))
        return result
