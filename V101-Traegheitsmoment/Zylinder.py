import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *

D = ufloat(0.02711, 0.00005)
I = ufloat(0.0030, 0.0003)
T1 = 2.29
T2 = 2.23
T3 = 2.23
T4 = 2.07
T5 = 2.07

print((T1**2 * D)/(4*np.pi**2))
print((T2**2 * D)/(4*np.pi**2))
print((T3**2 * D)/(4*np.pi**2))
print((T4**2 * D)/(4*np.pi**2))
print((T5**2 * D)/(4*np.pi**2))

I1 = ufloat(0.003601, 0.000007)
I2 = ufloat(0.003415, 0.000006)
I3 = ufloat(0.003415, 0.000006)
I4 = ufloat(0.002942, 0.000005)
I5 = ufloat(0.002942, 0.000005)

a = (I1+I2+I3+I4+I5)/5

print(a)
