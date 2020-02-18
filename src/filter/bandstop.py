from src.line.Line import Line
from src.filter.lowpass import low_pass_filter

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
