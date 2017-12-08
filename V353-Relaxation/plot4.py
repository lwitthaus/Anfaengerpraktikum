import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

w, A, phi = np.genfromtxt('amplitude.txt', unpack=True)

def f(phi, d):
   return np.arctan(d*phi) * 180/np.pi

x_plot = np.linspace(10, 35000, 5000)
params, covariance_matrix = curve_fit(f, w*2*np.pi, phi)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.xscale('log')
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(w*2*np.pi , phi, 'r.', label='Messwerte', Markersize=4)
plt.title('Phasenverschiebung in Abhängigkeit der Frequenz')
plt.legend()
plt.grid()
plt.xlabel(r'$w$/Hz')
plt.ylabel(r'$\varphi/$°')
plt.savefig('build/plot4.pdf')
