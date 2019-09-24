from src.drawable.Drawable import Drawable


class AdditionComposite(Drawable):

    def __init__(self, title, drawable, *args):
        self.drawable = drawable
        self.args = args
        super(AdditionComposite, self).__init__(title, drawable.getN())

    def calculateY(self):
        result = self.drawable.y
        for arg in self.args:
            result = result + arg.y
        return result
