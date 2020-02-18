from src.line.Line import Line

def mult(*args):
    list_args = list(args)
    title = ' * '.join([arg.title for arg in list_args])
    return MultiplicationComposite(title, list_args[0], *list_args[1:])

def mult_const(drawable, const):
    return Line(drawable.title, y=drawable.y * const)

class MultiplicationComposite(Line):

    def __init__(self, title, drawable, *args):
        self.drawable = drawable
        self.args = args
        super(MultiplicationComposite, self).__init__(title, drawable.getN())

    def calculateY(self):
        result = self.drawable.y
        for arg in self.args:
            result = result * arg.y
        return result
