from src.Canvas import Canvas
from src.IOController import IOController
from src.compositing.AdditionComposite import AdditionComposite
from src.compositing.AvgComposite import AvgComposite
from src.compositing.ConcatComposite import ConcatComposite
from src.drawable.Exp import Exp
from src.drawable.Harmonic import Harmonic
from src.drawable.Line import Line
from src.compositing.MultiplicationComposite import MultiplicationComposite
from src.drawable.MyRandom import MyRandom
from src.drawable.Random import Random

canvas = Canvas()
io = IOController()

N = 1000
FROM_NUM = -100
TO_NUM = 100

ascending_line = Line(title="Ascending line", N=N, k=3, b=2)
descending_line = Line(title="Descending line", N=N, k=-2, b=0)
exponential = Exp(title="Exponential", N=N, alpha=10e-3, beta=2)
concat = ConcatComposite(
    "Piecewize function",
    Line(title="", N=500, k=2, b=0),
    Line(title="", N=500, k=-1, b=1000),
)

random = Random(title="Random", N=N, fromNum=FROM_NUM, toNum=TO_NUM)
my_random = MyRandom(title="My random", N=N, fromNum=FROM_NUM, toNum=TO_NUM)

line_plus_random = AdditionComposite(
    "Line + Random",
    Random(title="", N=N, fromNum=FROM_NUM, toNum=TO_NUM),
    Line(title="", N=N, k=-1, b=1000)
)
line_x_random = MultiplicationComposite(
    "Line x Random",
    Random(title="", N=N, fromNum=FROM_NUM, toNum=TO_NUM),
    Line(title="", N=N, k=0.1, b=0)
)
avg_of_randoms = AvgComposite(
    "Average of randoms",
    *[Random(title="", N=N, fromNum=FROM_NUM, toNum=TO_NUM) for _ in range(10)]
)

garmonic = Harmonic(title="asd", N=N, A0=100, f0=11, delta_t=0.001)

drawables = enumerate([
    Harmonic(title="f=11", N=N, A0=100, f0=11, delta_t=0.001),
    Harmonic(title="f=110", N=N, A0=100, f0=110, delta_t=0.001),
    Harmonic(title="f=250", N=N, A0=100, f0=250, delta_t=0.001),
    Harmonic(title="f=510", N=N, A0=100, f0=510, delta_t=0.001)
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
