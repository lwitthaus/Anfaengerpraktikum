import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

w, A, phi = np.genfromtxt('amplitude.txt', unpack=True)

def f(w, d):
   return np.arctan(d*w*2*np.pi)*180/np.pi

x_plot = np.linspace(10, 35000, 5000)
params, covariance_matrix = curve_fit(f, w, phi)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.xscale('log')
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(w , phi, 'r.', label='Messwerte', Markersize=4)
plt.title('Phasenverschiebung in Abhängigkeit der Frequenz')
plt.legend()
plt.grid()
plt.xlim((10, 2*10**4))
plt.xlabel(r'$f$/Hz')
plt.ylabel(r'$\varphi/$°')
plt.savefig('build/plot4.pdf')
