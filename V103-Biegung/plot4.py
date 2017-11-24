import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

n, x, D = np.genfromtxt('beidseitig2.txt', unpack=True)
y = 4*(x*10**(-2))**3 - 12*0.554*(x*10**(-2))**2 + 9*0.554**2*x*10**(-2) - 0.554**3
plt.plot(y*10**3, D*10, 'r.', label='Biegung an Stelle x', Markersize=4)

def f(x, a, b):
   return a * x + b

x_plot = np.linspace(0.01,0.17)
params, covariance_matrix = curve_fit(f, y, D*10**(-2))
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(x_plot*10**3, f(x_plot, *params)*10**3, 'k-', label='Anpassungsfunktion', linewidth=0.5)
plt.title('Verhältnis Auslenkung zu Polynom des runden Stabes (x > L/2)')
plt.legend()
plt.grid()
plt.xlabel('$(4x^3 - 12Lx^2 + 9L^2x - L^3)$ / $10^{-3} m^3$')
plt.ylabel('$D_{B2}$(x) / $10^{-3} m')
print(params)
print(np.sqrt(np.diag(covariance_matrix)))

plt.savefig('build/Beidseitig2.pdf')
