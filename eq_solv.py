from scipy.optimize import fsolve
import math
import numpy as np
import matplotlib.pyplot as plt

def eq(p):
    x, y = p
    return (y - x**2 + 1, np.exp(x) - x*y + x - 1)

def eq2(x):
    return (x**2 - 1)

def eq3(x):
    return (np.exp(x)/x + 1 - 1/x)

if __name__ == '__main__':
    x1, y1 = fsolve(eq, (1,1))
    print(x1,y1)

    x = np.linspace(-9.5, 10, 210000)
    y = eq2(x)

    x2 = []
    y2 = []


    for i in range(len(x)):
        if ((np.exp(x[i]) - x[i]*y[i] + x[i] - 1) >= 0):
            x2.append(x[i])
            y2.append(y[i])
        else:
            #все отброшенные варианты
            print(np.exp(x[i]) - x[i]*y[i] + x[i] - 1)

    print(x2, y2)