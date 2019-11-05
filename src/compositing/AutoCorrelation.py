from src.drawable.Drawable import Drawable


class AutoCorrelation(Drawable):

    def __init__(self, title, drawable, start=0, end=None):
        self.drawable = drawable
        self.start = start
        self.end = drawable.getN() if end is None else end
        super(AutoCorrelation, self).__init__(title, drawable.getN())

    def calculateY(self):
        mean = self.drawable.getMean(self.drawable.y)
        result = [0.0] * self.end
        divider = 0
        for k in range(self.start,self.end):
            divider += (self.drawable.y[k] - mean) ** 2
        for funShift in range(self.start, self.end):
            temp = 0
            for k in range(0, self.end - funShift):
                temp += (self.drawable.y[k] - mean) * (self.drawable.y[k + funShift] - mean)
            temp /= divider
            result[funShift - self.start] = temp
        return result









