import math

from src.compositing.convolution import Convolution
from src.drawable.Drawable import Drawable
from src.util.common import N, create_array

def ecg(freq=10, amplitude=120, dt=0.005, interval=200, relaxation=15):
    return Cardiogram("Cardiogram", N, freq, amplitude, dt, interval, relaxation)

class Cardiogram(Drawable):

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
        return Drawable("", x=self.x, y=y)

    def delta(self):
        y = create_array(self.getN(), lambda i: 1 if i % self.interval == 0 else 0,)
        return Drawable("", x=self.x, y=y)

    def calculateY(self):
        return Convolution("", self.base(), self.delta()).y
