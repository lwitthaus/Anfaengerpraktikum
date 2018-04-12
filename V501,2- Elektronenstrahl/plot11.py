import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0
from scipy.optimize import curve_fit
from uncertainties import ufloat

U, D = np.genfromtxt('tabelle1.txt', unpack=True)
A, B = np.genfromtxt('tabelle2.txt', unpack=True)
E, F = np.genfromtxt('tabelle3.txt', unpack=True)
G, H = np.genfromtxt('tabelle4.txt', unpack=True)
I, J = np.genfromtxt('tabelle5.txt', unpack=True)
L = 0.143
N = 20
R = 0.282

def f(x, a, b):
   return a * x + b


x_plot = np.linspace(-40, 20)
params, covariance_matrix = curve_fit(f, U, D)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'r-', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(U, D, 'r.', label='Messwerte $U_B=200$V', Markersize=4)

params, covariance_matrix = curve_fit(f, A, B)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'b-', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.plot(A, B, 'b.', label='Messwerte $U_B=250$V', Markersize=4)

params, covariance_matrix = curve_fit(f, E, F)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'g-', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.plot(E, F, 'g.', label='Messwerte $U_B=300$V', Markersize=4)

params, covariance_matrix = curve_fit(f, G, H)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'y-', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.plot(G, H, 'y.', label='Messwerte $U_B=350$V', Markersize=4)

params, covariance_matrix = curve_fit(f, I, J)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'c-', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.plot(I, J, 'c.', label='Messwerte $U_B=400$V', Markersize=4)

plt.legend()
plt.grid()
plt.xlim((-40, 20))
plt.xlabel(r'$U_d/V$')
plt.ylabel(r'$D/$mm')
plt.savefig('build/plot11.pdf')
