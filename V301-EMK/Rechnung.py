import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *

Uk = 1.7
Ri = ufloat(16.3, 0.2)
Rv = 10*10**6

print(Uk*Ri/Rv)
print(Uk + Uk*Ri/Rv - Uk)
