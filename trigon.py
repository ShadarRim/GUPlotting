import numpy as np
import matplotlib.pyplot as plt
import math

def cosplot(k = 1, a = 1, b = 1):
    x = np.arange(-10, 10, 0.1)
    y = [0]*len(x)
    for i in range(len(x)):
        y[i] = k*math.cos(x[i] - a) + b
    return x,y

if __name__ == '__main__':
    x1, y1 = cosplot(0, 1, 1)
    x2, y2 = cosplot(1, 1, 1)
    x3, y3 = cosplot(2, -1, 4)

    plt.plot(x1, y1, x2, y2, x3, y3)
    plt.show()

