import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

phi, U, Uv = np.genfromtxt('phase.txt', unpack=True)

def f(phi, A, B, C):
   return A* np.cos(phi*2*np.pi / 360 + B) + C

x_plot = np.linspace(-10, 310, 400)
params, covariance_matrix = curve_fit(f, phi, Uv)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(phi , Uv, 'r.', label='Messwerte', Markersize=4)
plt.legend()
plt.grid()
plt.xlim((-10, 310))
plt.xlabel(r'$\phi / $grad')
plt.ylabel(r'$Uv/$mV')
plt.savefig('build/plot2.pdf')
