import math
import numpy as np
import matplotlib.pyplot as plt

x = 100
a = 0.01

eps = 0.001

while x < 500:
    a = 0.01
    while a < 0.02:
        #print(f'{x} {a} {np.sin(a*x)}')
        if (-1)*eps < np.sin(a*x) < eps:
            print(f'{x} {a}')
        a += eps
    x += eps

