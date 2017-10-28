import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

t, T, ln = np.genfromtxt('Verdampfungswaerme.txt', unpack=True)

plt.plot(T, ln, 'k.', label='ln($p_b$/$p_a$)', Markersize=4)

def f(x, a, b):
   return a * x + b

x_plot = np.linspace(0.0031,0.0034)
params, covariance_matrix = curve_fit(f, T, ln)
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Fit', linewidth=0.5)
plt.title('Verdampfungswärme')
plt.legend()
plt.grid()
plt.xlabel('1/T [1/K]')
plt.ylabel('ln($p_b$/$p_a$)')
print(params)
print(np.sqrt(np.diag(covariance_matrix)))

plt.savefig('build/Verdampfungswaerme.pdf')