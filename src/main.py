from src.Canvas import Canvas
from src.IOController import IOController
from src.compositing.AdditionComposite import add
from src.compositing.AvgComposite import avg
from src.compositing.ConcatComposite import concat
from src.compositing.MultiplicationComposite import mult
from src.compositing.hammingwindow import window
from src.compositing.inversedft import idft
from src.drawable.cardiogram import ecg
from src.drawable.itoprocess import ito
from src.util.buider import harmonic, const, rand, line, dft

canvas = Canvas()
io = IOController()

# INVERSE DFT
# drawables = enumerate([
#     harmonic(), const(0),
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

drawables = enumerate([
    const(0), const(0),
    const(0), const(0)
])

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
