import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp

U, N, I = np.genfromtxt('datenfit.txt', unpack=True)
F = np.sqrt(N)
R = unp.uarray([N],[F])
print(I*60/R)
