import copy

import numpy as np

from src.transform.fouriertransform import DiscreteFourierTransform
from src.transform.autocorrelation import AutoCorrelation
from src.transform.crosscorrelation import CrossCorrelation
from src.drawable.Drawable import Drawable
from src.util.common import N, FROM_NUM, TO_NUM, DEFAULT_CLONE
from src.drawable.Harmonic import Harmonic
from src.drawable.Line import Line
from src.drawable.Random import Random

# BASE

def line(k=-2, b=10):
    return Line("Trend", N=N, k=k, b=b)

def rand(start=FROM_NUM, end=TO_NUM):
    return Random("Random", N=N, fromNum=start, toNum=end)

def const(value=0, n=N):
    return Line("Const", N=n, k=0, b=value)

def harmonic(amplitude=10, frequency=15, delta_t=0.001, n=N):
    return Harmonic(title="Harmonic", N=n, A0=amplitude, f0=frequency, delta_t=delta_t)

# MODIFICATION

def shift(drawable, offset=100, clone=DEFAULT_CLONE):
    copied = copy.deepcopy(drawable) if clone else drawable
    copied.shift(offset)
    return copied

def spikes(drawable, count=10, size=3, clone=DEFAULT_CLONE):
    copied = copy.deepcopy(drawable) if clone else drawable
    copied.add_spikes(count=count, size_multiplier=size)
    return copied

def trunc(drawable, values):
    return Drawable(drawable.title, N=values, y=drawable.y[:values])

def sub(drawable, start, end=None):
    end = drawable.getN() if end is None else end
    return Drawable(drawable.title, N=end - start, y=drawable.y[start:end])

def absolute(drawable):
    return Drawable(drawable.title, y=np.abs(drawable.y))

# ANALYSIS

def fft(drawable):
    return trunc(Drawable("Spectrum", y=np.fft.fft(drawable.y)), values=int(drawable.getN() / 2))

def dft(drawable):
    return trunc(DiscreteFourierTransform("Spectrum", drawable), values=int(drawable.getN() / 2))

def anti_shift(drawable, y_min=FROM_NUM, y_max=TO_NUM, clone=DEFAULT_CLONE):
    copied = copy.deepcopy(drawable) if clone else drawable
    copied.suppress_spikes(y_min, y_max)
    return copied

def anti_spikes(drawable, clone=DEFAULT_CLONE):
    copied = copy.deepcopy(drawable) if clone else drawable
    copied.suppress_spikes()
    return copied

def anti_trend(drawable, window_size=3, clone=DEFAULT_CLONE):
    copied = copy.deepcopy(drawable) if clone else drawable
    copied.anti_trend(window_size)
    return copied

def auto(drawable):
    return AutoCorrelation("AutoCorrelation", drawable)

def cross(d1, d2, start=0, end=N):
    return CrossCorrelation("CrossCorrelation of "+d1.title+" and "+d2.title, d1, d2, start, end)
