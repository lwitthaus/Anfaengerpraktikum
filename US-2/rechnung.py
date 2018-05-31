import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *
import uncertainties.unumpy as unp
from scipy.stats import sem

n, t = np.genfromtxt('TMScan.txt', unpack=True)
h = 1/2*1485*t*10**(-4)
k = h*np.pi/6*(3*2.46**2 + h**2)

print(np.std(k))
print(np.mean(k))

v = ufloat(36.46, 1.49)
print (v*0.47)
