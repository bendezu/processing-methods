from src.Canvas import Canvas
from src.IOController import IOController
from src.compositing.ConcatComposite import concat
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
from src.util.buider import const, line, rand, harmonic, dft

canvas = Canvas()
io = IOController()

drawables = enumerate([
    ito(), const(),
    const(), const()
])

# # INVERSE DFT
# drawables = enumerate([
#     harmonic(), const(),
#     dft(harmonic()), idft(harmonic())
# ])

# HAMMING WINDOW
# initial = concat(harmonic(n=800), const(0, n=200))
# drawables = enumerate([
#     initial, window(initial),
#     dft(initial), dft(window(initial))
# ])

# CARDIOGRAM
# drawables = enumerate([
#     ecg(), const(0),
#     const(0), const(0)
# ])

# FILTERS
# drawables = enumerate([
#     lowpass(), dft(lowpass()),
#     highpass(), dft(highpass()),
#     bandpass(), dft(bandpass()),
#     bandstop(), dft(bandstop())
# ])

# pgp = io.read_from_dat("pgp_f4-1K-1ms.dat")
# pgp_lowpass = conv(pgp, lowpass(n=32, fCut=100))
# pgp_highpass = conv(pgp, highpass(n=32, fCut=100))
# pgp_bandpass = conv(pgp, bandpass(n=32, fCutLower=30, fCutUpper=150))
# pgp_bandstop = conv(pgp, bandstop(n=64, fCutLower=30, fCutUpper=150))
# drawables = enumerate([
#     pgp, dft(pgp),
#     pgp_lowpass, dft(pgp_lowpass),
#     pgp_highpass, dft(pgp_highpass),
#     pgp_bandpass, dft(pgp_bandpass),
#     pgp_bandstop, dft(pgp_bandstop),
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
