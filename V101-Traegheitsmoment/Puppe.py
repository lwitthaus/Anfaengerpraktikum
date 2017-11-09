import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *

D = ufloat(0.02711, 0.00005)
I = ufloat(0.0030, 0.0003)

T1 = 0.41
T2 = 0.41
T3 = 0.36
T4 = 0.50
T5 = 0.52
print('Arme angelegt:')
print((T1**2 * D)/(4*np.pi**2))
print((T2**2 * D)/(4*np.pi**2))
print((T3**2 * D)/(4*np.pi**2))
print((T4**2 * D)/(4*np.pi**2))
print((T5**2 * D)/(4*np.pi**2))
I1 = ufloat(0.00011543, 0.00000021)
I2 = ufloat(0.00011543, 0.00000021)
I3 = ufloat(0.00008900, 0.00000016)
I4 = ufloat(0.00017168, 0.00000032)
I5 = ufloat(0.00018568, 0.00000034)
a = (I1+I2+I3+I4+I5)/5
print(a)

T6 = 0.60
T7 = 0.55
T8 = 0.50
T9 = 0.64
T10 = 0.64
print('Arme gehoben:')
print((T6**2 * D)/(4*np.pi**2))
print((T7**2 * D)/(4*np.pi**2))
print((T8**2 * D)/(4*np.pi**2))
print((T9**2 * D)/(4*np.pi**2))
print((T10**2 * D)/(4*np.pi**2))
I6 = ufloat(0.0002472, 0.0000005)
I7 = ufloat(0.0002077, 0.0000004)
I8 = ufloat(0.0001717, 0.0000003)
I9 = ufloat(0.0002813, 0.0000005)
I10 = ufloat(0.0002813, 0.0000005)
b = (I6+I7+I8+I9+I10)/5
print(b)
