import numpy as np
import matplotlib.pyplot as plt
import math

def draw_circle_from_pos(x_cent = 1, y_cent = 1, r = 3):
    len1 = 1000
    x_l = x_cent - r
    x_r = x_cent + r

    len = (x_r - x_l)*len1

    x = np.linspace(x_l, x_r, len)

    y1 = [x_cent]*len
    y2 = [y_cent]*len

    for i in range(len):
            y1[i] = math.sqrt(r**2 - (x[i]-x_cent)**2) + y_cent
            y2[i] = -1 * (y1[i] - y_cent) + y_cent

    #y1 = math.sqrt((x-x_cent)**2-r**2) + y_cent

    plt.plot(x, y1, 'b', x, y2, 'b')

    plt.show()

def draw_ellipse_from_pos(x_cent = 0, y_cent = 0, x_ax = 3, y_ax = 2):
    len1 = 1000
    x_l = -1* x_ax
    x_r = x_ax
    len = (x_r - x_l)*len1

    x = np.linspace(x_l, x_r, len)

    y1 = [x_cent]*len
    y2 = [y_cent]*len

    for i in range(len):
        y1[i] = math.sqrt(y_ax**2 * (1 - x[i]**2/x_ax**2))
        y2[i] = (-1)*y1[i]
        x[i] += x_cent
        y1[i] += y_cent
        y2[i] += y_cent

    plt.plot(x, y1, 'b', x, y2, 'b')

    plt.show()

def draw_hyp_from_pos(x_cent = 0, y_cent = 0, x_ax = 3, y_ax = 2):
    len1 = 1000
    x_l = -5 * x_ax
    x_r = 5 * x_ax
    len = (x_r - x_l)*len1

    x = np.linspace(x_l, x_r, len)

    y1 = [x_cent]*len
    y2 = [y_cent]*len

    for i in range(len):
        if (x[i]**2/x_ax**2 - 1) >= 0:
            y1[i] = math.sqrt(y_ax**2 * (x[i]**2/x_ax**2 - 1))
            y2[i] = (-1)*y1[i]
            y1[i] += y_cent
            y2[i] += y_cent
        else:
            y1[i] = None
            y2[i] = None
        x[i] += x_cent


    plt.plot(x, y1, 'b', x, y2, 'b')

    plt.show()

if __name__ == '__main__':
    draw_circle_from_pos(1, 1, 3)
    draw_ellipse_from_pos(1, 1, 3, 2)
    draw_hyp_from_pos(1, 1, 3, 2)
