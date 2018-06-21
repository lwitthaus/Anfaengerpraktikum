import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0
from scipy.optimize import curve_fit
from uncertainties import ufloat

N = np.genfromtxt('statistik.txt', unpack=True)

plt.hist(N, 12, normed=5, facecolor='blue', alpha=0.75)
plt.savefig('build/hist.pdf')
