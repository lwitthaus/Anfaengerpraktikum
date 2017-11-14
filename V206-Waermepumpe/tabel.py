import numpy as np

t, T1, T2, pa, pb, W = np.genfromtxt('daten.txt', unpack=True)
t *= 60
T1 += 273.15
T2 += 273.15
pa += 1
pb += 1
pa *= 1e5
pb *= 1e5
einsdurchT1 = 1/T1
logarithmusp = np.log(pb/101325)
np.savetxt('datenneu.txt', np.transpose([t,T1,T2,pa,pb,W,einsdurchT1,logarithmusp]), fmt='%1.4f')
