import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp

a = ufloat(16789, 130)
b = ufloat(18646, 140)

print((b-a)/a*100/(700-320))
