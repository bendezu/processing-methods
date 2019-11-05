import numpy as np
import os
import struct
from src.drawable.Drawable import Drawable

DATA_FORMAT = ".dat"
FIGURE_FORMAT = ".png"
DELIMITER = ", "
INPUT_FOLDER = "input/"
OUTPUT_FOLDER = "output/"


class IOController:

    def clear_dirs(self):
        if os.path.exists(INPUT_FOLDER):
            for file in os.listdir(INPUT_FOLDER):
                os.unlink(INPUT_FOLDER + file)
        if os.path.exists(OUTPUT_FOLDER):
            for file in os.listdir(OUTPUT_FOLDER):
                os.unlink(OUTPUT_FOLDER + file)

    def writeToFile(self, drawable, ordinal):
        os.makedirs(INPUT_FOLDER, exist_ok=True)
        with open(INPUT_FOLDER + str(ordinal) + ". " + drawable.title + DATA_FORMAT, 'w+') as file:
            for i in range(len(drawable.x)):
                file.write(str(drawable.x[i]) + DELIMITER + str(drawable.y[i]) + "\n")

    def getDrawablesInDir(self):
        return enumerate(map(lambda file: self.readFromFile(file), os.listdir(INPUT_FOLDER)))

    def readFromFile(self, filename):
        x, y = np.loadtxt(INPUT_FOLDER + filename, delimiter=DELIMITER, unpack=True)
        return Drawable(filename[3:-len(DATA_FORMAT)], x=x, y=y)

    def savePlotToFile(self, figure, name):
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)
        figure.savefig(OUTPUT_FOLDER + name + FIGURE_FORMAT)

    def read_from_dat(self, filepath):
        with open(filepath, 'rb') as input_file:
            array_from_file = input_file.read()
        format = '{:d}f'.format(len(array_from_file) // 4)
        array_from_file = struct.unpack(format, array_from_file)
        return Drawable(filepath, N=len(array_from_file), y=array_from_file)
