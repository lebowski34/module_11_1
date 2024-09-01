import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, label='sin(x)')

plt.title('График функции sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()

plt.show()

data = np.random.randn(1000)
plt.hist(data, bins=30, alpha=0.5, color='g')
plt.title('Гистограмма случайных данных')
plt.show()

