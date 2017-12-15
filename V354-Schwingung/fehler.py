import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *
y = ufloat(954, 10)
T= 1/(2*np.pi * y)
#Abklingzeit
#print(T)

L = ufloat(10.11*10**(-3), 0.03*10**(-3))
#effektiv Widerstandes

#R = 4 * np.pi * y * L
#print(R)


r = ufloat(48.1, 0.1)
G = 50
#print(r + G)


#Güte
R2 = ufloat(509.5+50, 0.5)
C = ufloat(2.098*10**(-9), 0.006*10**(-9))
q = 1/(2*np.pi*34000*R2*C)
#print(q)


#Resonanzbreite
R = ufloat(121, 1)
#q = ufloat(4.34, 0.01)
w = 2.13 *10**(3)
n = R2/(L)
print(n)
