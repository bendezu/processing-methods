import os
import struct

import numpy as np
import pandas as pd
from scipy.io import wavfile

from src.drawable.Drawable import Drawable

DATA_FORMAT = ".dat"
FIGURE_FORMAT = ".png"
WAV_FORMAT = ".wav"
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

    def read_from_csv(self, filepath):
        df = pd.read_csv(INPUT_FOLDER + filepath)
        data = df['Open']
        return Drawable(filepath, N=len(data), y=data)

    def read_from_dat(self, filepath):
        with open(INPUT_FOLDER + filepath, 'rb') as input_file:
            array_from_file = input_file.read()
        format = '{:d}f'.format(len(array_from_file) // 4)
        array_from_file = np.array(struct.unpack(format, array_from_file))
        return Drawable(title=filepath, N=len(array_from_file), y=array_from_file)

    def read_from_wav(self, filepath):
        rate, data = wavfile.read(INPUT_FOLDER + filepath)
        self.last_rate = rate
        x = np.zeros(len(data))
        for i in range(1, len(data)):
            x[i] = x[i - 1] + 1 / rate
        return rate, Drawable(filepath, x=x, y=data)

    def save_to_wav(self, drawable, rate=None):
        r = self.last_rate if rate is None else rate
        filename = drawable.title if drawable.title.endswith(WAV_FORMAT) else drawable.title + WAV_FORMAT
        wavfile.write(OUTPUT_FOLDER + filename, r, drawable.y.astype(np.int16))
