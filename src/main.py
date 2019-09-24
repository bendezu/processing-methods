from src.Canvas import Canvas
from src.IOController import IOController
from src.drawable.AdditionCompositeDrawable import AdditionCompositeDrawable
from src.drawable.AvgComposite import AvgComposite
from src.drawable.Line import Line
from src.drawable.MultiplicationCompositeDrawable import MultiplicationCompositeDrawable
from src.drawable.MyRandom import MyRandom
from src.drawable.Random import Random

NUM_FIRST = "1. "
NUM_SECOND = "2. "
NUM_THIRD = "3. "
NUM_FOURTH = "4. "

canvas = Canvas()
io = IOController()
N = 1000

drawables = [
    Random(title=NUM_FIRST + "+k", N=N, fromNum=-100, toNum=100),
    AvgComposite(NUM_SECOND + "AVG",
        Random(title="", N=N, fromNum=-100, toNum=100),
        Random(title="", N=N, fromNum=-100, toNum=100),
        Random(title="", N=N, fromNum=-100, toNum=100),
        Random(title="", N=N, fromNum=-100, toNum=100),
        Random(title="", N=N, fromNum=-100, toNum=100),
        Random(title="", N=N, fromNum=-100, toNum=100),
        Random(title="", N=N, fromNum=-100, toNum=100),
        Random(title="", N=N, fromNum=-100, toNum=100),
        Random(title="", N=N, fromNum=-100, toNum=100),
        Random(title="", N=N, fromNum=-100, toNum=100),
    ),
    MultiplicationCompositeDrawable(title=NUM_THIRD + "Composite +k",
        first=Random(title="", N=N, fromNum=-100, toNum=100),
        second=Line(title="", N=N, k=0.1, b=0)
    ),
    MultiplicationCompositeDrawable(title=NUM_FOURTH + "Composite -k",
        first=Random(title="", N=N, fromNum=-100, toNum=100),
        second=Line(title="", N=N, k=-1, b=1000)
    )
]

io.clearDirs()

for drawable in drawables:
    io.writeToFile(drawable)

drawables = io.getDrawablesInDir()

for i, drawable in enumerate(drawables):
    # drawable.normalize(S=10)
    # drawable.add_spikes(count=10, size_multiplier=2)
    # drawable.shift(start=200, end=700, offset=150)
    canvas.add_drawable(drawable)
figure = canvas.plot()

# io.savePlotToFile(figure, "result")

# стационарность Не каждый с каждым
# divide(multiply(Drawable, Int), Int)
# композитный \/\/\