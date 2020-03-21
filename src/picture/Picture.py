from matplotlib.colors import Normalize

from src.Plotable import Plotable
from src.line.Line import Line


class Picture(Plotable):

    def __init__(self, title, matrix):
        self.title = title
        self.matrix = matrix

    def get_title(self):
        return self.title

    def plot_on(self, subplot):
        subplot.imshow(self.matrix, cmap="gray", norm=Normalize(0, 255))

    def get_line(self, index):
        return Line("Pic line" + str(index), y=self.matrix[index])
