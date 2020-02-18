import numpy as np

from src.line.Line import Line

def avg(*args):
    list_args = list(args)
    title = ' ~ '.join([arg.title for arg in list_args])
    return AvgComposite(title, list_args[0], *list_args[1:])

class AvgComposite(Line):

    def __init__(self, title, drawable, *args):
        self.drawable = drawable
        self.args = args
        super(AvgComposite, self).__init__(title, drawable.getN())

    def calculateY(self):
        result = self.drawable.y
        for arg in self.args:
            result = result + arg.y
        return result / len(self.args)
