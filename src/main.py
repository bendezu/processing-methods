import copy

from src.Canvas import Canvas
from src.IOController import IOController
from src.compositing.ConcatComposite import concat
from src.compositing.MultiplicationComposite import mult, mult_const
from src.line.Line import Line
from src.line.cardiogram import ecg
from src.line.itoprocess import ito
from src.line.wienerprocess import wiener
from src.filter.bandpass import bandpass
from src.filter.bandstop import bandstop
from src.filter.halflowpass import halflowpass
from src.filter.highpass import highpass
from src.filter.lowpass import lowpass
from src.transform.convolution import conv
from src.transform.hammingwindow import window
from src.transform.inversedft import idft
from src.util.buider import const, line, rand, harmonic, dft, sub, fft, absolute, cross, auto, anti_trend

canvas = Canvas()
io = IOController()

drawables = enumerate([
    const(), const(),
    const(), const()
])

for i, drawable in drawables:
    canvas.add_drawable(drawable)
figure = canvas.plot()

io.savePlotToFile(figure, "result")

# TODO fix myrandom
# TODO rename line metrics
# TODO dft adjust scale
# TODO suppress spikes by sliding window
