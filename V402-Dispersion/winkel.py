import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *
import uncertainties.unumpy as unp

r, l = np.genfromtxt('winkel.txt', unpack=True)
pr, pl = np.genfromtxt('phi.txt', unpack=True)

print('Eta:')
print(180-(r-l))
print('Phi:')
print(1/2*(pl-pr))
