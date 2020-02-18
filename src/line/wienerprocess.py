import math

from src.line.Line import Line
from src.util.common import N

import numpy as np

def wiener(c=1, s0=100, n=N):
    return WienerItoProcess("USA stock market", n, c, s0)

class WienerItoProcess(Line):

    def __init__(self, title, N, c, s0):
        self.s0 = s0
        self.c = c
        super(WienerItoProcess, self).__init__(title, N)

    def calculateY(self):
        n = self.getN()
        dt = 1 / n
        w = np.random.uniform(low=0, high=1, size=(n,))
        for i in range(len(w)):
            w[i] = 1 if w[i] > 0.5 else -1
        dx = self.c * math.sqrt(dt)
        dw = w * dx
        S = np.zeros(n)
        S[0] = self.s0
        for i in range(1, len(dw)):
            prev_x = self.x[i-1] * dt
            S[i] = self.mu(S[i-1], prev_x) * dt + self.sigma(S[i-1], prev_x) * dw[i] + S[i-1]
        return S

    def mu(self, y, x):
        return 8*y + x

    def sigma(self, y, x):
        return y * x
