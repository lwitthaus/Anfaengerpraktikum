import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

n, T1, T2, pa, pb, p = np.genfromtxt('daten.txt', unpack=True)

def f(x, a, b, c):
   return a * x**2 + b*x + c

x_plot = np.linspace(0,2000)
params, covariance_matrix = curve_fit(f, n*60, T1)
plt.plot(x_plot, f(x_plot, *params), 'r-', label='Fit', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))

params, covariance_matrix = curve_fit(f, n*60, T2)
plt.plot(x_plot, f(x_plot, *params), 'b-', label='Fit', linewidth=0.5)

plt.plot(n*60,T1, 'r.', label='T1', Markersize=4)
plt.plot(n*60,T2, 'b.', label='T2', Markersize=4)
plt.title('Temperaturen')
plt.legend()
plt.grid()
plt.xlabel('t / s')
plt.ylabel('T / °C')
print(params)
print(np.sqrt(np.diag(covariance_matrix)))

plt.savefig('build/Temperaturen.pdf')
