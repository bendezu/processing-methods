from src.Canvas import Canvas
from src.IOController import IOController
from src.drawable.itoprocess import ito
from src.util.buider import harmonic, const, rand, add, line

canvas = Canvas()
io = IOController()


drawables = enumerate([
    rand(), ito(a=0, b=-0.002, c=1, d=70),
    const(10), add(line(), harmonic())
])

io.clear_dirs()

for i, drawable in drawables:
    io.writeToFile(drawable, ordinal=i + 1)

drawables = io.getDrawablesInDir()

for i, drawable in drawables:
    canvas.add_drawable(drawable)
figure = canvas.plot()

io.savePlotToFile(figure, "result")

# TODO fix myrandom
# TODO rename drawable metrics
# TODO dft adjust scale
# TODO suppress spikes by sliding window
