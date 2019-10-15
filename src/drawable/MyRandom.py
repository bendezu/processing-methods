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
        center = (self.toNum + self.fromNum) / 2
        diameter = (self.toNum - self.fromNum) / 2
        return math.sin(time.clock() * time.time() % 10000000) * diameter + center
