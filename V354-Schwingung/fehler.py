import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *
y = ufloat(954, 10)
T= 1/(2*np.pi * y)
#Abklingzeit
#print(T)

L = ufloat(10.11*10**(-3), 0.03*10**(-3))
#effektiv Widerstandes

R = 4 * np.pi * y * L
print(R)


r = ufloat(48.1, 0.1)
G = 50
print(r + G)
