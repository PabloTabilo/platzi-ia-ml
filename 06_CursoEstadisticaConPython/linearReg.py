import numpy as np
import matplotlib.pyplot as plt

x = np.array(list(range(100)))
y = np.random.normal(50,15,100)

coeffs = np.polyfit(x,y,1)
print(coeffs)

m, b = coeffs
est_y = (m * x) + b
plt.plot(x,est_y)
plt.scatter(x,y)
plt.show()