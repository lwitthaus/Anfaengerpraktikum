import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

n, a, t = np.genfromtxt('daten.txt', unpack=True)

def f(x, c, b):
   return c * x + b

x_plot = np.linspace(0,0.03)
params, covariance_matrix = curve_fit(f, (a/100)**2, t**2)
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Fit Schwingdauer', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))

plt.plot((a/100)**2,t**2, 'r.', label='Schwingdauer', Markersize=4)
plt.title('Verhältnis Abstand zu Schwingdauer')
plt.legend()
plt.grid()
plt.xlabel('$a^2$ / $m^2$')
plt.ylabel('$t^2$ / $s^2$')

plt.savefig('build/plot.pdf')
