import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *
import uncertainties.unumpy as unp
C = ufloat(2.098*10**(-9), 0.006 *10**(-9))
L = ufloat(10.11*10**(-3), 0.03*10**(-3))
R = unp.sqrt(4*L/C)
print(R)
