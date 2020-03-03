import copy
import numpy as np

from src.Canvas import Canvas
from src.IOController import IOController
from src.compositing.ConcatComposite import concat
from src.compositing.MultiplicationComposite import mult, mult_const
from src.line.Line import Line
from src.picture.postprocessing import neg, gamma, log, transform
from src.picture.scaling import scale
from src.picture.statistic import histogram, cdf
from src.transform.convolution import conv
from src.transform.hammingwindow import window
from src.util.buider import const, line, rand, sub, absolute, cross, auto, anti_trend

canvas = Canvas()
io = IOController()

def lesson1():
    img = io.read_from_jpg("grace.jpg")
    return np.array([
        (img, scale(img, ratio=3, strategy="nearest-neighbor"), scale(img, ratio=0.5, strategy="nearest-neighbor")),
        (img, scale(img, ratio=3, strategy="bilinear"), scale(img, ratio=0.5, strategy="bilinear"))
    ])

def lesson2():
    img1 = io.read_from_jpg("image1.jpg")
    img2 = io.read_from_jpg("image2.jpg")
    return np.array([
        (neg(img1), neg(img2)),
        (gamma(img1, C=1, gamma=1.1), gamma(img2, C=1, gamma=0.3)),
        (log(img1, C=1), log(img2, C=1))
    ])

def lesson3():
    img = io.read_from_jpg("HollywoodLC-1.jpg")
    img2 = transform(img, cdf(img))
    return np.array([
        (img, histogram(img)),
        (img, cdf(img)),
        (img2, histogram(img2))
    ])

plotables = lesson1()
canvas.set_plotables(plotables)
figure = canvas.plot()

io.savePlotToFile(figure, "result")

# TODO deconvolution
# TODO image scale up(bilinear)/down
# TODO invert cdf
