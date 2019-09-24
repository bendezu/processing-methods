from src.drawable.Drawable import Drawable


class MultiplicationCompositeDrawable(Drawable):

    def __init__(self, title, first, second):
        self.first = first
        self.second = second
        super(MultiplicationCompositeDrawable, self).__init__(title, first.x.getN())

    def calculateY(self):
        return self.first.y * self.second.y
