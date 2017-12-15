import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp

R = 509.5 + 50
L = 10.11*10**(-3)
C = 2.098*10**(-9)

w, U0, UC, a, U, phi = np.genfromtxt('phase2.txt', unpack=True)

def f(w):
       return 1/np.sqrt((1-L*C*(w*2*np.pi)**2)**2 + (w*2*np.pi)**2 * (R*C)**2)

x_plot = np.linspace(26000, 41000, 1000)
plt.plot((x_plot), f(x_plot), 'b-', label='Theoriekurve')


#print(np.sqrt(np.diag(covariance_matrix)))
#print('U_0 gleich ', params[0], ' +- ', errors[0])
#print('my gleich ', params[1], ' +-' , errors[1])
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot((w) , U, 'r.', label='Messwerte', Markersize=4)
plt.axhline(2.63, color='green', linestyle=':')
plt.axvline(28500, color='blue', linestyle=':')
plt.axvline(37500, color='blue', linestyle=':')
#plt.xscale("log")
plt.title('Spannungsamplituden in Abhängigkeit von der Frequenz')
plt.legend()
plt.grid()
plt.xlim((26000,41000 ))
plt.xlabel(r'$f/$Hz')
plt.ylabel(r'$\frac{U_C}{U_0}$')
plt.savefig('build/plot5.pdf')
