import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

f, A, phi = np.genfromtxt('amplitude.txt', unpack=True)

def fit(f, d):
   return 1/(np.sqrt(1 + d**2  * (f*2*np.pi)**2))

x_plot = np.linspace(0, 35000, 5000)
params, covariance_matrix = curve_fit(fit, f, A/3.6, p0 = 0.000001)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, fit(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.xscale('log')
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(f , A/3.6, 'r.', label='Messwerte', Markersize=4)
plt.title('Spannungsamplitude in Abhängigkeit der Kreisfrequenz')
plt.legend()
plt.grid()
plt.xlabel(r'$f$/Hz')
plt.ylabel(r'$(A/U_0$')
plt.savefig('build/plot2.pdf')
