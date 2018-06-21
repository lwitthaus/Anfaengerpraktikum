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


g = np.random.normal(np.mean(N), np.std(N), 10000)
p = np.random.poisson(np.mean(N), 10000)
plt.hist([g,N,p], 15, label=['Gauß', 'Messwerte', 'Poisson'], alpha=1, normed=1)
plt.legend()
plt.savefig('build/hist.pdf')
