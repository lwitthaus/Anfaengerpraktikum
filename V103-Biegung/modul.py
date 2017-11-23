import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *
#Elastizitäsmodul runder Stab (einseitig)
m = 4.6995
g = 9.81
#I = 4.909 * (10**(-10))
#a = ufloat(0.059, 0.001)
#print(m*g/(2*I*a))

#Elastizitäsmodul quadratischer Stab (einseitig)
#I = 8.333 * (10**(-10))
#c = ufloat(0.0458, 0.0007)
#print(m*g/(2*I*c))

I = 4.909 * (10**(-10))
e = ufloat(0.0178, 0.0007)

print(m*g/(48*I*e))
