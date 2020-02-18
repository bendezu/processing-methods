from src.line.Line import Line


class Trend(Line):

    def __init__(self, title, N, k, b):
        self.k = k
        self.b = b
        super(Trend, self).__init__(title, N)

    def calculateY(self):
        return self.k * self.x + self.b
