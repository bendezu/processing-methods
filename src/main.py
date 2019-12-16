from src.Canvas import Canvas
from src.IOController import IOController
from src.compositing.ConcatComposite import concat
from src.compositing.MultiplicationComposite import mult, mult_const
from src.drawable.Drawable import Drawable
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

# canvas.plot_interactive_ito(ito())

drawables = enumerate([
    io.read_from_csv("MSFT.csv"), const(),
    io.read_from_csv("AAPL.csv"), io.read_from_csv("PG.csv")
])

# wav = io.read_from_wav("ma.wav")
# lowpassed = conv(wav, lowpass(dt=1/22050, fCut=250))
# drawables = enumerate([
#     wav, absolute(fft(wav)),
#     lowpassed, const()
# ])
# io.save_to_wav(const(), 10000)

for i, drawable in drawables:
    canvas.add_drawable(drawable)
figure = canvas.plot()

io.savePlotToFile(figure, "result")

# TODO fix myrandom
# TODO rename drawable metrics
# TODO dft adjust scale
# TODO suppress spikes by sliding window
