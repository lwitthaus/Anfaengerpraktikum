import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

D, P = np.genfromtxt('daten2.txt', unpack=True)

def f(x, c, b):
   return c * x + b

x_plot = np.linspace(0,80)
params, covariance_matrix = curve_fit(f, P, D)
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(P ,D, 'r.', label='Schwingdauer', Markersize=4)
plt.title('Verhältnis Auslenkung zu Polynom des quadratischen Stabes')
plt.legend()
plt.grid()
plt.xlabel(r'$(Lx^2 -\frac{x^3}{3})$ / $m$')
plt.ylabel(r'$D_Q(x)$ / $m$')
plt.savefig('build/plot2.pdf')
