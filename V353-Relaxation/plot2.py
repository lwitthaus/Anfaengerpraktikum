import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

w, A, phi = np.genfromtxt('amplitude.txt', unpack=True)

def f(w, d):
   return 1/(np.sqrt(1 + d**2  * w**2))

x_plot = np.linspace(10, 5000, 5000)
params, covariance_matrix = curve_fit(f, w, A/3.6)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.xscale('log')
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(w , A/3.6, 'r.', label='Messwerte', Markersize=4)
plt.title('Spannungsamplitude in Abhängigkeit der Frequenz')
plt.legend()
plt.grid()
plt.xlabel(r'$w$/Hz')
plt.ylabel(r'$(A/U_0/$V')
plt.savefig('build/plot2.pdf')
