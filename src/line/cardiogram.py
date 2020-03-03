import math

from src.transform.convolution import Convolution
from src.line.Line import Line
from src.util.common import N, create_array

def ecg(freq=10, amplitude=120, dt=0.005, interval=200, relaxation=15):
    return Cardiogram("Cardiogram", N, freq, amplitude, dt, interval, relaxation)

def base(f=10, k=15, dt=0.005, n=N):
    multiplier = 2 * math.pi * f * dt
    y = create_array(n, lambda i: math.sin(multiplier * i) * math.exp(-k * dt * i))
    return Line("", y=y)

def delta(interval=200, n=N):
    y = create_array(n, lambda i: 1 if i % interval == 0 else 0,)
    return Line("", y=y)

class Cardiogram(Line):

    def __init__(self, title, N, f, a, dt, interval, k):
        self.f = f
        self.a = a
        self.dt = dt
        self.interval = interval
        self.k = k
        super(Cardiogram, self).__init__(title, N)

    def base(self):
        multiplier = 2 * math.pi * self.f * self.dt
        y = create_array(self.getN(), lambda i: math.sin(multiplier * i) * math.exp(-self.k * self.dt * i))
        return Line("", x=self.x, y=y)

    def delta(self):
        y = create_array(self.getN(), lambda i: 1 if i % self.interval == 0 else 0,)
        return Line("", x=self.x, y=y)

    def calculateY(self):
        return Convolution("", self.base(), self.delta()).y
