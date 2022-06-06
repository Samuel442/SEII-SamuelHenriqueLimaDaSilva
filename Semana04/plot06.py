import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.scatter(x,y)
plt.show()

import numpy as np
x1 = np.arange(-1000,1000,1)
print(x1)

plt.plot(x1, -x1**3+4)
plt.show()
  