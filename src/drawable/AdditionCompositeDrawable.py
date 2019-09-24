from src.drawable.Drawable import Drawable


class AdditionCompositeDrawable(Drawable):

    def __init__(self, title, first, second):
        self.first = first
        self.second = second
        super(AdditionCompositeDrawable, self).__init__(title, first.getN())

    def calculateY(self):
        return self.first.y + self.second.y
