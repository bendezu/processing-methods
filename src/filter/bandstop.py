import copy

from src.line.Line import Line
from src.filter.lowpass import low_pass_filter
from scipy import signal

from src.picture.Picture import Picture


def bandstop(n=128, dt=0.001, fCutLower=50, fCutUpper=100):
    return Line("Band Stop Filter", y=band_stop_filter(n, dt, fCutLower, fCutUpper))

def band_stop_filter(n, dt, fCutLower, fCutUpper):
    lpfLower = low_pass_filter(n, dt, fCutLower)
    lpfUpper = low_pass_filter(n, dt, fCutUpper)
    for i in range(len(lpfLower)):
        if i == n:
            lpfLower[i] = 1 + lpfLower[i] - lpfUpper[i]
        else:
            lpfLower[i] = lpfLower[i] - lpfUpper[i]
    return lpfLower

def bsf_line(line: Line, lowcut, highcut):
    y = _bsf(line.y, lowcut, highcut, fs=len(line.y))
    return Line(title="bsf of " + line.title, y=y)

def bsf_pic(picture: Picture, lowcut, highcut, clone=True):
    pic = copy.deepcopy(picture) if clone else picture
    rows, cols = picture.matrix.shape
    for i in range(rows):
        row = picture.matrix[i]
        pic.matrix[i] = _bsf(row, lowcut, highcut, len(row))
    return pic

def _bsf(data, lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = signal.butter(order, [low, high], btype='bandstop')
    return signal.lfilter(b, a, data)
