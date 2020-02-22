import copy
import numpy as np

from src.Canvas import Canvas
from src.IOController import IOController
from src.compositing.ConcatComposite import concat
from src.compositing.MultiplicationComposite import mult, mult_const
from src.line.Line import Line
from src.picture.postprocessing import neg, gamma, log
from src.transform.convolution import conv
from src.transform.hammingwindow import window
from src.transform.inversedft import idft
from src.util.buider import const, line, rand, harmonic, dft, sub, fft, absolute, cross, auto, anti_trend

canvas = Canvas()
io = IOController()

img1 = io.read_from_jpg("image1.jpg")
img2 = io.read_from_jpg("image2.jpg")

plotables = np.array([
    (neg(img1), neg(img2)),
    (gamma(img1, C=1, gamma=1.1), gamma(img2, C=1, gamma=0.3)),
    (log(img1, C=1), log(img2, C=1))
])
canvas.set_plotables(plotables)
figure = canvas.plot()

io.savePlotToFile(figure, "result")

# TODO fix myrandom
# TODO rename line metrics
# TODO dft adjust scale
# TODO suppress spikes by sliding window
