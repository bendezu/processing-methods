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
from src.picture.postprocessing import neg, gamma, log
from src.transform.convolution import conv
from src.transform.hammingwindow import window
from src.transform.inversedft import idft
from src.util.buider import const, line, rand, harmonic, dft, sub, fft, absolute, cross, auto, anti_trend

canvas = Canvas()
io = IOController()

img1 = io.read_from_jpg("image1.jpg")
img2 = io.read_from_jpg("image2.jpg")

drawables = enumerate([
    img1, img2,
    neg(img1), neg(img2),
    gamma(img1, C=1, gamma=1.1), gamma(img2, C=1, gamma=0.3),
    log(img1, C=1), log(img2, C=1)
])

for i, drawable in drawables:
    canvas.add_drawable(drawable)
figure = canvas.plot()

io.savePlotToFile(figure, "result")

# TODO fix myrandom
# TODO rename line metrics
# TODO dft adjust scale
# TODO suppress spikes by sliding window
