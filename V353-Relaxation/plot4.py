import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

w, A, phi = np.genfromtxt('amplitude.txt', unpack=True)

def f(phi, d):
   return np.arctan(d*phi)

x_plot = np.linspace(10, 5000, 5000)
params, covariance_matrix = curve_fit(f, w, phi)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.xscale('log')
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(w , phi, 'r.', label='Messwerte', Markersize=4)
plt.title('Spannungsamplitude zu dem Zeitpunkt t')
plt.legend()
plt.grid()
plt.xlabel(r'$w$/Hz')
plt.ylabel(r'$A/$V')
plt.savefig('build/plot3.pdf')
