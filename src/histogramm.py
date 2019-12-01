import matplotlib.pyplot as plt
import numpy as np

from src.util.buider import rand

x = rand().y
x2 = np.random.normal(size=1000)
plt.hist(x2, bins=40)
plt.ylabel('Probability')
plt.show()
