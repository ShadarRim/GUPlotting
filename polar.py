import numpy as np
import matplotlib.pyplot as plt
import math

def ploar_to_decart(r, phi):
    x = [0]*len(r)
    y = [0]*len(r)

    for i in range(len(r)):
        x = r[i] * math.cos(phi)
        y = r[i] * math.sin(phi)

    return x, y

def polar_circle():
    theta = np.arange(0, 2, 1/180)*np.pi
    r = 3
    plt.polar(theta, [r]*len(theta))

    plt.show()

def polar_stright():
    r = np.arange(0, 5, 0.1)
    ang = 2/180*np.pi
    theta = [ang]*len(r)

    plt.polar(theta,r)
    plt.show()

if __name__ == '__main__':
    polar_circle()
    polar_stright()