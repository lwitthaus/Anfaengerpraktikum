import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *
import uncertainties.unumpy as unp

a=[0.351, 0.313, 0.304]
print(np.mean(a))
print(np.std(a))
