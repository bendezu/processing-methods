from src.drawable.Drawable import Drawable


class AdditionComposite(Drawable):

    def __init__(self, title, drawable, *args):
        self.drawable = drawable
        self.args = args
        super(AdditionComposite, self).__init__(title, drawable.getN())

    def calculateY(self):
        accum = self.drawable.y
        for arg in self.args:
            accum = accum + arg.y
        return accum
