from src.Canvas import Canvas
from src.IOController import IOController
from src.compositing.AdditionComposite import AdditionComposite
from src.compositing.DiscreteFourierTransform import DiscreteFourierTransform
from src.drawable.Harmonic import Harmonic
from src.util.common import N, FROM_NUM, TO_NUM
from src.drawable.Line import Line
import copy

canvas = Canvas()
io = IOController()

harmonic_11 = Harmonic(title="Harmonic f=11", N=N, A0=100, f0=11, delta_t=0.001)
harmonic_110 = Harmonic(title="Harmonic f=110", N=N, A0=100, f0=110, delta_t=0.001)
harmonic_250 = Harmonic(title="Harmonic f=250", N=N, A0=100, f0=250, delta_t=0.001)
harmonic_510 = Harmonic(title="Harmonic f=510", N=N, A0=100, f0=510, delta_t=0.001)
dft_11 = DiscreteFourierTransform("DFT 11", harmonic_11)
dft_110 = DiscreteFourierTransform("DFT 110", harmonic_110)
dft_250 = DiscreteFourierTransform("DFT 250", harmonic_250)
dft_510 = DiscreteFourierTransform("DFT 510", harmonic_510)

polyharmonic = AdditionComposite(
    "Polyharmonic",
    Harmonic(title="", N=N, A0=25, f0=11, delta_t=0.001),
    Harmonic(title="", N=N, A0=35, f0=41, delta_t=0.001),
    Harmonic(title="", N=N, A0=30, f0=141, delta_t=0.001),
)

def harmonic_shift():
    graph = Harmonic(title="Harmonic shift", N=N, A0=100, f0=110, delta_t=0.001)
    graph.shift(offset=100)
    return graph

def harmonic_spikes():
    graph = Harmonic(title="Harmonic spikes", N=N, A0=100, f0=110, delta_t=0.001)
    graph.add_spikes(count=10, size_multiplier=3)
    return graph

def harmonic_anti_shift():
    graph = harmonic_shift()
    graph.anti_shift()
    return graph

def harmonic_anti_spikes():
    graph = harmonic_spikes()
    graph.suppress_spikes(FROM_NUM, TO_NUM)
    return graph


drawables = enumerate([
    harmonic_shift(), harmonic_spikes(), harmonic_anti_shift(), harmonic_anti_spikes()
])

io.clear_dirs()

for i, drawable in drawables:
    io.writeToFile(drawable, ordinal=i + 1)

drawables = io.getDrawablesInDir()

for i, drawable in drawables:
    # drawable.normalize(S=10)
    # drawable.add_spikes(count=10, size_multiplier=2)
    # drawable.shift(offset=150, start=200, end=700)
    canvas.add_drawable(drawable)
figure = canvas.plot()

io.savePlotToFile(figure, "result")

# TODO fix myrandom
# TODO rename drawable metrics
# TODO dft adjust scale
# TODO suppress spikes by sliding window
