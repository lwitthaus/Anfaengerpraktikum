import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp

a0 = ufloat(2.93, 0.01)
a1 = ufloat(5.9*10**4, 0.3*10**4)
l = np.array([404.6 ,439.8 ,480.0 ,502.5 ,546.1 ,577.0 ,615.8 ,656.7])
n = np.array([1.813, 1.805, 1.784, 1.781, 1.771, 1.764, 1.760, 1.750])

d = 0
for i in range (0,8):
    d += (n[i]**2 - a0 - a1/l[i]**2)**2

print(1/6*d)

a0 = ufloat(3.4, 0.03)
a1 = ufloat(8.1*10**(-7), 0.9*10**(-7))

d = 0
for i in range (0,8):
    d += (n[i]**2 - a0 + a1*l[i]**2)**2

print(1/6*d)
