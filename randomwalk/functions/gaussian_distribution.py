import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - sigma, mu + sigma, 100)
y = stats.norm.pdf(x, mu, sigma)
plt.plot(x, y)
plt.title("Gaussian Distribution hack")
plt.show()
