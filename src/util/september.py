from src.compositing.AdditionComposite import AdditionComposite
from src.compositing.AvgComposite import AvgComposite
from src.compositing.ConcatComposite import ConcatComposite
from src.compositing.MultiplicationComposite import MultiplicationComposite
from src.drawable.Exp import Exp
from src.drawable.Line import Line
from src.drawable.MyRandom import MyRandom
from src.drawable.Random import Random
from src.util.common import N, FROM_NUM, TO_NUM

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
