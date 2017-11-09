import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *

d1 = ufloat(0.03266, 0.00019)
d2 = ufloat(0.03592, 0.00021)
d3 = ufloat(0.02613, 0.00015)
d4 = ufloat(0.02613, 0.00015)
d5 = ufloat(0.02351, 0.00014)
d6 = ufloat(0.02667, 0.00016)
d7 = ufloat(0.02519, 0.00015)
d8 = ufloat(0.02531, 0.00015)
d9 = ufloat(0.02504, 0.00015)
d10 = ufloat(0.02449, 0.00014)


a = (d1+d2+d3+d4+d5+d6+d7+d8+d9+d10)/10


print(a)
