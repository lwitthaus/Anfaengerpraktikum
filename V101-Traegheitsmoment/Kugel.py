import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *

D = ufloat(0.02711, 0.00005)
I = ufloat(0.0030, 0.0003)
T1 = 1.56
T2 = 1.53
T3 = 1.64
T4 = 1.58
T5 = 1.60

print((T1**2 * D)/(4*np.pi**2))
print((T2**2 * D)/(4*np.pi**2))
print((T3**2 * D)/(4*np.pi**2))
print((T4**2 * D)/(4*np.pi**2))
print((T5**2 * D)/(4*np.pi**2))

I1 = ufloat(0.0016712, 0.0000031)
I2 = ufloat(0.0016075, 0.0000030)
I3 = ufloat(0.0018470, 0.0000034)
I4 = ufloat(0.0017143, 0.0000032)
I5 = ufloat(0.0017580, 0.0000032)

a = (I1+I2+I3+I4+I5)/5

print(a)
