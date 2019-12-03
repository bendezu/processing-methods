from src.drawable.Drawable import Drawable
from src.filter.bandstop import band_stop_filter

def bandpass(n=128, dt=0.001, fCutLower=50, fCutUpper=100):
    return Drawable("Band Pass Filter", y=band_pass_filter(n, dt, fCutLower, fCutUpper))

def band_pass_filter(n, dt, fCutLower, fCutUpper):
    return band_stop_filter(n, dt, fCutUpper, fCutLower)
