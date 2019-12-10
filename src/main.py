from src.Canvas import Canvas
from src.IOController import IOController
from src.compositing.ConcatComposite import concat
from src.compositing.MultiplicationComposite import mult, mult_const
from src.drawable.cardiogram import ecg
from src.drawable.itoprocess import ito
from src.filter.bandpass import bandpass
from src.filter.bandstop import bandstop
from src.filter.halflowpass import halflowpass
from src.filter.highpass import highpass
from src.filter.lowpass import lowpass
from src.transform.convolution import conv
from src.transform.hammingwindow import window
from src.transform.inversedft import idft
from src.util.buider import const, line, rand, harmonic, dft, sub, fft, absolute

canvas = Canvas()
io = IOController()

# a_us = io.read_from_csv("a.us.txt")
# aa_us = io.read_from_csv("aa.us.txt")
# aaap_us = io.read_from_csv("aaap.us.txt")
# aaba_us = io.read_from_csv("aaba.us.txt")
# drawables = enumerate([
#     sub(a_us, 1000, 2000), sub(aa_us, 0, 1000),
#     aaap_us, sub(aaba_us, 2000, 3000)
# ])

# io.clear_dirs()
#
# for i, drawable in drawables:
#     io.writeToFile(drawable, ordinal=i + 1)
#
# drawables = io.getDrawablesInDir()

for i, drawable in drawables:
    canvas.add_drawable(drawable)
figure = canvas.plot()

io.savePlotToFile(figure, "result")

# TODO fix myrandom
# TODO rename drawable metrics
# TODO dft adjust scale
# TODO suppress spikes by sliding window
