import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp

a0 = ufloat(16789, 130)
b0 = ufloat(18646, 140)
a1 = ufloat(6.4*10**(-2), 0.3*10**(-2))
b1 = ufloat(260, 2)
c = a1*320+b1
d = a1*700+b1
print((d-c)/c*100/(700-320))
print((b0-a0)/a0*100/(700-320))
