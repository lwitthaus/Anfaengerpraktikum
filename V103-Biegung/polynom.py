import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *
#Runder Stab (einseitig)
#x = np.array([40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240,260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480])
#L = 0.5
#print(((L * (x*10**(-3))**2) - ((x * 10**(-3))**(3) * 1/3)) * 10**3)
#
#print('----------------------------')
#quadratischer Stab einseitig

#runder Stab beidseitig
n, x, D = np.genfromtxt('beidseitig1.txt', unpack=True)
print((3*0.554**2*x*10**(-2) - 4*(x*10**(-2))**3)*10**3)
