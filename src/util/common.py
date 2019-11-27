import numpy as np

N = 1000
FROM_NUM = -100
TO_NUM = 100
DEFAULT_CLONE = True

def create_array(n, factory):
    arr = np.zeros(n)
    for i in range(n):
        arr[i] = factory(i)
    return arr
