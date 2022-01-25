import numpy as np
import matplotlib.pyplot as plt

from scipy.special import fresnel

# change plot theme from matplotlib library
plt.style.use('ggplot')

# define space
t = np.linspace(-10,10, 1000)
x,y = fresnel(t)

# plot visual
plt.plot(x,y, c='black')
plt.show()
