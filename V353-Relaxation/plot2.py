import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

w, A, phi = np.genfromtxt('amplitude.txt', unpack=True)

def f(w, d):
   return 1/(np.sqrt(1 + d  * w**2))

x_plot = np.linspace(0, 5000)
params, covariance_matrix = curve_fit(f, w, A)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(w , A, 'r.', label='Spannungsamplitude zum Zeitpunkt t', Markersize=4)
plt.title('Spannungsamplitude zu dem Zeitpunkt t')
plt.legend()
plt.grid()
plt.xlabel(r'$\omega/$Hz')
plt.ylabel(r'$A/$V')
plt.savefig('build/plot2.pdf')
