import numpy as np
import matplotlib.pyplot as plt 

n_pts = 1001

def PDF(r):
    return ((r**4)/24)*np.exp(-r)

r = np.linspace(0, 15, n_pts)
P = np.zeros(n_pts)

P = PDF(r)

fig, ax = plt.subplots()
ax.plot(r, P, color="orange")
ax.grid(True, which="both")
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

ax.set_xlabel(r"$\frac{r}{a_0}$", fontsize="20")
ax.set_ylabel(r"$P(r)=(rR(r))^2$", fontsize="20")
plt.show()