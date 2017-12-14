import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp

R = ufloat(509.5, 0.1)


f1, U0, UC, a, U, phi = np.genfromtxt('phase.txt', unpack=True)

def f(f1, A, B):
   return 1/unp.sqrt((1-L*C*(f1*2*np.pi)**2)**2 + (f1*2*np.pi)**2 * (R*C)**2)

x_plot = np.linspace(0, 400, 400)
params, covariance_matrix = curve_fit(f, np.log(f1*2*np.pi), U)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
#print(np.sqrt(np.diag(covariance_matrix)))
#print('U_0 gleich ', params[0], ' +- ', errors[0])
print('my gleich ', params[1], ' +-' , errors[1])
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(np.log(f1*2*np.pi) , U, 'r.', label='Messwerte', Markersize=4)
plt.title('Spannungsamplituden in Abhängigkeit der Frequenz')
plt.legend()
plt.grid()
plt.xlabel(r'$f/$s')
plt.ylabel(r'$\frac{U_C}{U_0}$')
plt.savefig('build/plot2.pdf')
