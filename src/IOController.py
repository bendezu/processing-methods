import numpy as np
import os
from src.drawable.Drawable import Drawable

DATA_FORMAT = ".dat"
FIGURE_FORMAT = ".png"
DELIMITER = ", "
INPUT_FOLDER = "../input/"
OUTPUT_FOLDER = "../output/"


class IOController:

    def clearDirs(self):
        for file in os.listdir(INPUT_FOLDER):
            os.unlink(INPUT_FOLDER + file)
        for file in os.listdir(OUTPUT_FOLDER):
            os.unlink(OUTPUT_FOLDER + file)

    def writeToFile(self, drawable):
        with open(INPUT_FOLDER + drawable.title + DATA_FORMAT, 'w') as file:
            for i in range(len(drawable.x)):
                file.write(str(drawable.x[i]) + DELIMITER + str(drawable.y[i]) + "\n")

    def getDrawablesInDir(self):
        return map(lambda file: self.readFromFile(file), os.listdir(INPUT_FOLDER))

    def readFromFile(self, filename):
        x, y = np.loadtxt(INPUT_FOLDER + filename, delimiter=DELIMITER, unpack=True)
        return Drawable(filename, x=x, y=y)

    def savePlotToFile(self, figure, name):
        figure.savefig(OUTPUT_FOLDER + name + FIGURE_FORMAT)
