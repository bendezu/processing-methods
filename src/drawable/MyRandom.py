import math
import time

from src.drawable.Drawable import Drawable


class MyRandom(Drawable):

    def __init__(self, title, N, fromNum, toNum):
        self.fromNum = fromNum
        self.toNum = toNum
        super(MyRandom, self).__init__(title, N)

    def calculateY(self):
        return [self.getRand() for _ in range(len(self.x))]

    def getRand(self):
        return math.sin(time.clock() * 1000000)
