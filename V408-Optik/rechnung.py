import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp
from scipy import stats

#e, g1, b1, g2, b2 = np.genfromtxt('bessel.txt', unpack=True)
#d1 = g1 - b1
#d2 = g2 - b2


#k = (e**2 - d1**2)/(4*e)
#l = (e**2 - d2**2)/(4*e)
#print('erste Brennweiten')
#print(k)
#print(np.mean(k))
#print(stats.sem(k))
#print('zweite Brennweiten')
#print(l)
#print(np.mean(l))
#print(stats.sem(l))

#e, g1, b1, g2, b2 = np.genfromtxt('besselrot.txt', unpack=True)
#d1 = g1 - b1
#d2 = g2 - b2

#k = (e**2 - d1**2)/(4*e)
#l = (e**2 - d2**2)/(4*e)
#print('erste Brennweiten')
#print(k)
#print(np.mean(k))
#print(stats.sem(k))
#print('zweite Brennweiten')
#print(l)
#print(np.mean(l))
#print(stats.sem(l))

e, g1, b1, g2, b2 = np.genfromtxt('besselblau.txt', unpack=True)
d1 = g1 - b1
d2 = g2 - b2


k = (e**2 - d1**2)/(4*e)
l = (e**2 - d2**2)/(4*e)
print('erste Brennweiten')
print(k)
print(np.mean(k))
print(stats.sem(k))
print('zweite Brennweiten')
print(l)
print(np.mean(l))
print(stats.sem(l))
