import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *

#R_2 = ufloat(500, 1)
#R_v = ufloat(0.473, 0.002)
#R_x = R_2 * R_v
#print(R_x)
#
#R_q = ufloat(1000, 2)
#R_w = ufloat(0.232, 0.001)
#R_y = R_q * R_w
#print(R_y)
#
#R_e = ufloat(332, 1)
#R_r = ufloat(0.715, 0.004)
#R_z = R_e * R_r
#print(R_z)
#
#
#a = np.std([236.5, 232.0, 237.4])
#print(a)

#zweiter Widerstand, Wert 12
R_2 = ufloat(500, 1)
R_v = ufloat(0.748, 0.004)
R_x = R_2 * R_v
print(R_x)

R_q = ufloat(1000, 2)
R_w = ufloat(0.357, 0.002)
R_y = R_q * R_w
print(R_y)

R_e = ufloat(332, 1)
R_r = ufloat(1.128, 0.006)
R_z = R_e * R_r
print(R_z)

a = np.std([374.0, 357.0, 374.5])
print(a)
