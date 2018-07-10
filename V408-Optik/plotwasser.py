import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0
from scipy.optimize import curve_fit
from uncertainties import ufloat

g, b = np.genfromtxt('datenwasser.txt', unpack=True)



#print(1/(1/g + 1/b))
def f(x, a, b):
   return a * x + b

x_plot = np.linspace(0, 17)
#params, covariance_matrix = curve_fit(f, 12.5, 56.8)
#errors = np.sqrt(np.diag(covariance_matrix))
#plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
#print(params)
#print(np.sqrt(np.diag(covariance_matrix)))
plt.gcf().subplots_adjust(bottom=0.18)
for i in range(0, 9, 1):
    plt.plot([0, g[i]], [b[i], 0], 'bx-')
plt.legend()
plt.grid()
#plt.xlim((10, 11))
plt.ylabel(r'$b / $cm')
plt.xlabel(r'$g / $cm')
plt.axvline(x=8.05, linewidth=0.5)
plt.axhline(y=8.05, linewidth=0.5)
plt.savefig('build/plot2.pdf')
