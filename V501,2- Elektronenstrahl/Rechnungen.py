import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties.umath import *

a = ufloat(8.97*10**3, 0.12*10**3)
b = ufloat(7.06*10**3, 0.10*10**3)
c = (a*np.sqrt(8*250))**2
d = (b*np.sqrt(8*400))**2
I = 0.08
print(mu_0*8/np.sqrt(125)*20*I/0.282)
print(1.76/1.6)
