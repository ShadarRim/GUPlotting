import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 210000)
y = 2*x
y2 = (-1/2)*x

plt.plot(x, y)
plt.plot(x, y2)

plt.xlabel("x")
plt.ylabel("y")

plt.xlim(-1, 1)
plt.ylim(-1, 1)

#визуальное отображение зависит от масштаба графика, а не только от математики

plt.show()