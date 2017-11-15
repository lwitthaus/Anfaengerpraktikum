import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *
#Massendurchsätze
L = ufloat(18830, 190)
T_1 = ufloat(-0.01170, 0.00030)
T_2 = ufloat(-0.00949, 0.00030)
T_3 = ufloat(-0.00729, 0.00030)
T_4 = ufloat(-0.00509, 0.00030)
m_1 = (750+16720) * T_1 * 120.9 / L
m_2 = (750+16720) * T_2 * 120.9 / L
m_3 = (750+16720) * T_3 * 120.9 / L
m_4 = (750+16720) * T_4 * 120.9 / L
#print(m_1, m_2, m_3, m_4)

#Kompressorleistung
p_a = np.array([440000, 400000, 380000, 370000])
p_b = np.array([860000, 940000, 1080000, 1150000])
m = np.array([m_1, m_2, m_3, m_4])
r = np.array([23100, 21000, 19900, 19400])
k = 1.14
N = 1 /0.14 * (p_b * (p_a/p_b)**(1/k)-p_a)*(1/r) * m
print(N)
