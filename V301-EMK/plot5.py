import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

P, R = np.genfromtxt('leistung.txt', unpack=True)
U0 = 1.34
Ri = 16.3
def f(R):
    return R*U0**2 /(R+Ri)**2 *10**3


x_plot = np.linspace(0, 100, 400)
plt.plot((x_plot), f(x_plot), 'b-', label='Theoriekurve')
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(R , P, 'r.', label='Messwerte', Markersize=4)
plt.title('Leistung der Monozelle')
plt.legend()
plt.grid()
plt.xlim((0, 80))
plt.xlabel(r'$R_a/ $ Ω')
plt.ylabel(r'$P/ \mathrm{mW}$')
plt.savefig('build/plot5.pdf')
