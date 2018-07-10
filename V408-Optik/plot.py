import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0
from scipy.optimize import curve_fit
from uncertainties import ufloat

g, b, B = np.genfromtxt('daten1.txt', unpack=True)
#a = np.array([[12.5, 0]  [12.0, 0]  [11.5, 0] [13.5, 0]  [14.0, 0]  [14.5, 0]  [15.0, 0]  [15.5, 0]  [16.0, 0] [16.5, 0]])
c = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#b1 = (0, 56.8)
#b2 = (0, 72.0)
#b3 = (0, 97.1)
#b4 = (0, 40.8)
#b5 = (0, 36.6)
#b6 = (0, 32.9)
#b7 = (0, 30.8)
#b8 = (0, 29.0)
#b9 = (0, 27.9)
#b10 = (0, 25.5)

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
#plt.plot(g, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'r.', label='Messwerte', Markersize=4)
#plt.plot([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], b, 'r.', Markersize=4)
plt.legend()
plt.grid()
#plt.xlim((10, 11))
plt.ylabel(r'$b / $cm')
plt.xlabel(r'$g / $cm')
plt.axvline(x=10.35, linewidth=0.5)
plt.axhline(y=10.35, linewidth=0.5)
plt.axvline(x=10, color='k', linewidth=0.5)
plt.axhline(y=10, color='k', linewidth=0.5)
plt.savefig('build/plot.pdf')



u, v = np.genfromtxt('datenwasser.txt', unpack=True)

print(b/g)
print(B/2.8)
