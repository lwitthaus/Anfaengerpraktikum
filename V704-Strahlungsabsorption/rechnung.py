import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *
import uncertainties.unumpy as unp

a1 = ufloat(-9.82, 1.66)
a2 = ufloat(-0.20, 0.17)
b1 = ufloat(6.07, 0.68)
b2 = ufloat(-0.16, 0.17)
R = (b2-b1)/(a1-a2)*10**(-1)
print(R)
print(1.92*unp.sqrt(R**2+0.22*R))
