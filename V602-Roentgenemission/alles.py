import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from matrix2latex import matrix2latex

A, B = np.genfromtxt('brom.txt', unpack=True)
E, F = np.genfromtxt('quecksilber.txt', unpack=True)
G, H = np.genfromtxt('stronzium.txt', unpack=True)
I, J = np.genfromtxt('zirkonium.txt', unpack=True)
K, L = np.genfromtxt('bragg.txt', unpack=True)

m = np.zeros((41, 10))

temp = np.zeros(41-A.size)
A = np.concatenate((A, temp))
m[:,0] = np.zeros(41) + A

temp = np.zeros(41-B.size)
B = np.concatenate((B, temp))
m[:,1] = np.zeros(41) + B

temp = np.zeros(41-E.size)
E = np.concatenate((E, temp))
m[:,2] = np.zeros(41) + E

temp = np.zeros(41-F.size)
F = np.concatenate((F, temp))
m[:,3] = np.zeros(41) + F

temp = np.zeros(41-G.size)
G = np.concatenate((G, temp))
m[:,4] = np.zeros(41) + G

temp = np.zeros(41-H.size)
H = np.concatenate((H, temp))
m[:,5] = np.zeros(41) + H

temp = np.zeros(41-I.size)
I = np.concatenate((I, temp))
m[:,6] = np.zeros(41) + I

temp = np.zeros(41-J.size)
J = np.concatenate((J, temp))
m[:,7] = np.zeros(41) + J

temp = np.zeros(41-K.size)
K = np.concatenate((K, temp))
m[:,8] = np.zeros(41) + K

temp = np.zeros(41-L.size)
L = np.concatenate((L, temp))
m[:,9] = np.zeros(41) + L

t = matrix2latex(m, format='%.1f')
print(t)
