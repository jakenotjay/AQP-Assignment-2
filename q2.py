import numpy as np 
import matplotlib.pyplot as plt

n_pts = 1001
x = np.linspace(-1, 3, n_pts)

def E(x):
    return x**2 - (2*x)

y = E(x)

fig, ax = plt.subplots()
ax.plot(x, y, label="L^2 - 2L", color="orange")
ax.grid(True, which="both")
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

ax.set_xlabel("L")
ax.set_ylabel("hbar^2/2I")
ax.legend(loc="upper right")
plt.show()


