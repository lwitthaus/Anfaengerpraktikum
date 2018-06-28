import numpy as np
import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp
from scipy import optimize
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import correlated_values
from matrix2latex import matrix2latex



def theory(x, A0, x_0, b):
    return (A0 * b * np.sinc(b * np.sin((x - x_0)/(l)) / l_welle))**2


def theory2(x, A0, x_0, b, spaltabstand):
    #return (2 * A_0 * np.cos(np.pi*spaltabstand*np.sin((x - x_0)/(l))/l_welle) * np.sinc(b * np.sin((x - x_0)/(l)) / l_welle))**2
    return (2 * np.cos(np.pi*spaltabstand*np.sin((x - x_0)/(l))/l_welle))**2*theory(x, A0, x_0, b)

l=1.01 #Abstand Spalt Detektor in meter
l_welle=635*1e-9 #Wellenlänge in meter... irgendwie will er lambda nicht akzeptieren :D

I_d=0.26*1e-9 #Dunkelstrom 1 in Ampere


b_1=0.075*1e-3 #spaltbreite in meter Einzelspalt
b_2=0.15*1e-3 #spaltbreite in meter dünner Doppelspalt
b_3=0.15*1e-3 #spaltbreite in meter breiter Doppelspalt
g_2=0.25*1e-3 #Spaltabstand des ersten Doppelspaltes in meter
g_3 = 0.5 *1e-3 #Spaltabstand des zweiten Doppelspaltes in meter

x_1, I_1 = np.genfromtxt('einzelspalt.txt', unpack=True) #s/mm I/nA
x_1 *= 1e-3 #s/m
I_1 *= 1e-6 #I/A
I_1 -=I_d  #Bereinigung Dunkelstrom
slinspace = np.linspace(0.010, 0.040, 500)


params1, covariance_matrix1 = optimize.curve_fit(theory, x_1, I_1, p0=[7.2, 0.004, 0.00009])

A_0, s_0, b = correlated_values(params1, covariance_matrix1)

print('Jetzt kommt der Einzelspalt')
print('A_0 =', A_0)
print('s_0 =', s_0)
print('b =', b)

# errors = np.sqrt(np.diag(covariance_matrix))

# print('A_0 =', params[0], '+-', errors[0])
# print('s_0=', params[1], '+-', errors[1])
# print('b =', params[2], '+-', errors[2])

# A_0 = ufloat(params[0], errors[0])
# s_0 = ufloat(params[1], errors[1])
# b = ufloat(params[2], errors[2])

plt.plot(slinspace*1e3, theory(slinspace, *params1)*1e6, 'k-', label='Ausgleichsfunktion')

plt.plot(x_1*1e3, I_1*1e6, 'r.', label='Messwerte')

plt.xlabel(r'$x/$mm')
plt.ylabel(r'$I/\mu$A')
plt.legend()
plt.grid()
plt.autoscale(enable=True, axis='x', tight=True)
plt.savefig('build/einfachspalt.pdf')

plt.clf()



x_2, I_2 = np.genfromtxt('doppelspalt1.txt', unpack=True) #s/mm I/nA
x_2 *= 1e-3 #s/m
I_2 *= 1e-6 #I/A
I_2 -=I_d  #Bereinigung Dunkelstrom

#params2, covariance_matrix2 = optimize.curve_fit(theory2, x_2, I_2, p0=[2700, 23, 0.000085, 0.00021])
params2, covariance_matrix2 = optimize.curve_fit(theory2, x_2, I_2, p0=[2700, 23, 0.000100, 0.00027])
A_0, s_0, b, spaltabstand = correlated_values(params2, covariance_matrix2)

print('Jetzt kommt der erste Doppelspalt')
print('A_0 =', A_0)
print('s_0 =', s_0)
print('b =', b)

#plt.plot(x_2*1e3, I_2*1e6, 'rx', label='Messwerte')
#
#plt.plot(slinspace*1e3, theory(slinspace, *params2)*1e6, 'k-', label='Ausgleichsfunktion')

plt.plot(x_2*1e3, I_2*1e6, 'r.', label='Messwerte')

plt.plot(slinspace*1e3, theory2(slinspace, *params2)*1e6, 'k-', label='Ausgleichsfunktion')


plt.xlabel(r'$x/$mm')
plt.ylabel(r'$I/\mu$A')
#plt.tight_layout()
plt.legend()
plt.grid()
plt.autoscale(enable=True, axis='x', tight=True)
plt.savefig('build/doppelspalt_1.pdf')

plt.clf()


x_3, I_3 = np.genfromtxt('doppelspalt2.txt', unpack=True) #s/mm I/nA ##################################
x_3 *= 1e-3 #s/m
I_3 *= 1e-6 #I/A
I_3 -=I_d  #Bereinigung Dunkelstrom
slinspace = np.linspace(0, 0.050, 500)

params3, covariance_matrix3 = optimize.curve_fit(theory2, x_3, I_3, p0=[4, 24, 1.5*1e-3, 1e-3])

A_0, s_0, b, spaltabstand = correlated_values(params3, covariance_matrix3)

print('Jetzt kommt der zweite Doppelspalt')
print('A_0 =', A_0)
print('s_0 =', s_0)
print('b =', b)
print('spaltabstand =', spaltabstand)

plt.plot(x_3*1e3, I_3*1e6, 'r.', label='Messwerte')

plt.plot(slinspace*1e3, theory2(slinspace, *params3)*1e6, 'k-', label='Ausgleichsfunktion')

plt.xlabel(r'$x/$mm')
plt.ylabel(r'$I/\mu$A')
plt.tight_layout()
plt.legend()
plt.grid()
plt.autoscale(enable=True, axis='x', tight=True)
plt.savefig('build/doppelspalt_2.pdf')
plt.clf()
