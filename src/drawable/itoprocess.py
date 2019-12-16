from src.drawable.Drawable import Drawable
from src.util.common import N

import numpy as np

def ito(a=0, b=-0.002, c=1, d=70, n=N):
    return ItoProcess("USA stock market", n, a, b, c, d)

class ItoProcess(Drawable):

    def __init__(self, title, N, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        super(ItoProcess, self).__init__(title, N)

    def calculateY(self):
        m = np.exp(self.b * self.x)
        s = self.d * np.sin(self.x / self.d)
        r = np.random.uniform(low=0, high=self.c, size=(len(self.x),))
        return self.a * self.c + self.x * m + self.d * s * r
