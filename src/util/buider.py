import copy

import numpy as np

from src.transform.fouriertransform import DiscreteFourierTransform
from src.transform.autocorrelation import AutoCorrelation
from src.transform.crosscorrelation import CrossCorrelation
from src.line.Line import Line
from src.util.common import N, FROM_NUM, TO_NUM, DEFAULT_CLONE, scale_array
from src.line.Harmonic import Harmonic
from src.line.Trend import Trend
from src.line.Random import Random

# BASE

def line(k=-2, b=10):
    return Trend("Trend", N=N, k=k, b=b)

def rand(start=FROM_NUM, end=TO_NUM):
    return Random("Random", N=N, fromNum=start, toNum=end)

def const(value=0, n=N):
    return Trend("Const", N=n, k=0, b=value)

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
    return Line(drawable.title, N=values, y=drawable.y[:values])

def sub(drawable, start, end=None):
    end = drawable.getN() if end is None else end
    return Line(drawable.title, N=end - start, y=drawable.y[start:end])

def absolute(drawable):
    return Line(drawable.title, y=np.abs(drawable.y))

# ANALYSIS

def diff(line: Line):
    return Line("diff of " + line.title, y=np.diff(line.y.astype("int32")))

def fft(drawable):
    return absolute(trunc(Line("Spectrum", y=np.fft.fft(drawable.y)), values=int(drawable.getN() / 2)))

def dft(drawable: Line, scale=False):
    result = trunc(DiscreteFourierTransform("dft of " + drawable.title, drawable), values=int(drawable.getN() / 2))
    if scale:
        result.x = scale_array(result.x, right=0.5)
    return result

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
    return CrossCorrelation("Cross of "+d1.title+" and "+d2.title, d1, d2, start, end)
