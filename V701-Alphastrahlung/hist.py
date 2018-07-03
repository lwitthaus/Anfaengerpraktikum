import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0
from scipy.optimize import curve_fit
from uncertainties import ufloat
import math

N = np.genfromtxt('statistik.txt', unpack=True)

#print(np.mean(N))

q = np.mean(N)
r = np.mean(N**2)
print(q)
print(np.std(N))
print(r-q**2)


g = np.random.normal(np.mean(N/10), np.std(N/10), 10000)
#p = np.random.poisson(np.mean(N), 10000)
plt.hist([N/10,g], 15, label=['Messwerte','Gaußverteilung'], alpha=1, normed=1)
plt.legend()
plt.ylabel(r'Normierte Häufigkeit')
plt.xlabel(r'Zählrate N / $\frac{1}{s}$')
plt.gcf().subplots_adjust(bottom=0.18)
plt.savefig('build/hist.pdf')
