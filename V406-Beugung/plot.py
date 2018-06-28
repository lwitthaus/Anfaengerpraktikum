import numpy as np
import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp
from scipy import optimize
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import correlated_values
from matrix2latex import matrix2latex


# Note that this piece of shit sinc-function from numpy is actually normalized sinc: np.sinc(x)=sin(pix)/pix
# nice to know...


def theory(zeta, A0, zeta_0, b):
    return (A0 * b * np.sinc(b * np.sin((zeta - zeta_0)/(l)) / l_welle))**2


def theorycentered(zeta, A0, b):
    return (A0 * b * np.sinc(b * np.sin((zeta/l) / l_welle)))**2


def theory2(zeta, A0, zeta_0, b, spaltentfernung):
    #return (2 * A_0 * np.cos(np.pi*spaltentfernung*np.sin((zeta - zeta_0)/(l))/l_welle) * np.sinc(b * np.sin((zeta - zeta_0)/(l)) / l_welle))**2
    return (2 * np.cos(np.pi*spaltentfernung*np.sin((zeta - zeta_0)/(l))/l_welle))**2*theory(zeta, A0, zeta_0, b)

l=1.01 #Abstand Spalt Detektor in meter
l_welle=635*1e-9 #Wellenlänge in meter... irgendwie will er lambda nicht akzeptieren :D

I_d=0.26*1e-9 #Dunkelstrom 1 in Ampere


b_1=0.075*1e-3 #spaltbreite in meter Einzelspalt
b_2=0.15*1e-3 #spaltbreite in meter dünner Doppelspalt
b_3=0.15*1e-3 #spaltbreite in meter breiter Doppelspalt
g_2=0.25*1e-3 #Spaltabstand des ersten Doppelspaltes in meter
g_3 = 0.5 *1e-3 #Spaltabstand des zweiten Doppelspaltes in meter

s_1, I_1 = np.genfromtxt('einzelspalt.txt', unpack=True) #s/mm I/nA
s_1 *= 1e-3 #s/m
I_1 *= 1e-6 #I/A
I_1 -=I_d  #Bereinigung Dunkelstrom
slinspace = np.linspace(0.010, 0.040, 500)


params1, covariance_matrix1 = optimize.curve_fit(theory, s_1, I_1, p0=[7.2, 0.004, 0.00009])

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

plt.plot(s_1*1e3, I_1*1e6, 'rx', label='Messwerte')

plt.xlabel(r'$s/$mm')
plt.ylabel(r'$I/\mu$A')
#plt.tight_layout()
plt.legend()
plt.grid()
plt.autoscale(enable=True, axis='x', tight=True)
plt.savefig('build/einfachspalt.pdf')

plt.clf()



s_2, I_2 = np.genfromtxt('doppelspalt1.txt', unpack=True) #s/mm I/nA
s_2 *= 1e-3 #s/m
I_2 *= 1e-6 #I/A
I_2 -=I_d  #Bereinigung Dunkelstrom

params2, covariance_matrix2 = optimize.curve_fit(theory2, s_2, I_2, p0=[2700, 23, 0.000085, 0.00021])

A_0, s_0, b, spaltentfernung = correlated_values(params2, covariance_matrix2)

print('Jetzt kommt der erste Doppelspalt')
print('A_0 =', A_0)
print('s_0 =', s_0)
print('b =', b)

#plt.plot(s_2*1e3, I_2*1e6, 'rx', label='Messwerte')
#
#plt.plot(slinspace*1e3, theory(slinspace, *params2)*1e6, 'k-', label='Ausgleichsfunktion')

plt.plot(s_2*1e3, I_2*1e6, 'rx', label='Messwerte')

plt.plot(slinspace*1e3, theory2(slinspace, *params2)*1e6, 'k-', label='Ausgleichsfunktion')


plt.xlabel(r'$s/$mm')
plt.ylabel(r'$I/\mu$A')
#plt.tight_layout()
plt.legend()
plt.grid()
plt.autoscale(enable=True, axis='x', tight=True)
plt.savefig('build/doppelspalt_1.pdf')

plt.clf()


s_3, I_3 = np.genfromtxt('doppelspalt2.txt', unpack=True) #s/mm I/nA ##################################
s_3 *= 1e-3 #s/m
I_3 *= 1e-6 #I/A
I_3 -=I_d  #Bereinigung Dunkelstrom

params3, covariance_matrix3 = optimize.curve_fit(theory2, s_3, I_3, p0=[4, 22, 0.00015, 0.0005])

A_0, s_0, b, spaltentfernung = correlated_values(params3, covariance_matrix3)

print('Jetzt kommt der zweite Doppelspalt')
print('A_0 =', A_0)
print('s_0 =', s_0)
print('b =', b)
print('spaltentfernung =', spaltentfernung)

plt.plot(s_3*1e3, I_3*1e6, 'rx', label='Messwerte')

plt.plot(slinspace*1e3, theory2(slinspace, *params3)*1e6, 'k-', label='Ausgleichsfunktion')

plt.xlabel(r'$s/$mm')
plt.ylabel(r'$I/\mu$A')
plt.tight_layout()
plt.legend()
plt.grid()
plt.autoscale(enable=True, axis='x', tight=True)
plt.savefig('build/doppelspalt_2.pdf')
plt.clf()

## Hier sollte man irgendwie die Amplituden gescheit normieren
#faktor = np.max(I_1) / np.max(I_3)
#I_1 = I_1 / faktor
#
## Dann den Zentrumspunkt shiften
#s_1 += 0.569*1e-3
#s_3 += 0.254*1e-3
#
## Erneut fitten, da jetzt anders zentriert
#
##params1, covariance_matrix1 = optimize.curve_fit(theory, s_1, I_1, p0=[5, 0, 1e-3])
#
##A_0, s_0, b = correlated_values(params1, covariance_matrix1)
#
##print('Jetzt kommt der korrigierte Einzelspalt')
##print('A_0 =', A_0)
##print('s_0 =', s_0)
##print('b =', b)
#
##params3, covariance_matrix3 = optimize.curve_fit(theory2, s_3, I_3, p0=[4, -0.2, 1.5e-3, 1e-3])
#
## Dann in einem Plot geschlossen darstellen
#
#params1[1] = 0
#params3[1] = 0
#print(I_1)
#
##plt.plot(s_1*1e3, I_1*1e9, 'rx', label='Messwerte Einzelspalt')
##plt.plot(slinspace*1e3, theory(slinspace, *params1)*1e9/faktor, 'r-', label='Ausgleichsfunktion Einzelspalt')
##plt.plot(s_3*1e3, I_3*1e9, 'kx', label='Messwerte Doppelspalt')
##plt.plot(slinspace*1e3, theory2(slinspace, *params3)*1e9, 'k-', label='Ausgleichsfunktion Doppelspalt')
##
##plt.xlabel(r'$s/$mm')
##plt.ylabel(r'$I/$nA')
##plt.tight_layout()
##plt.legend()
##plt.legend(loc = 'upper left', fontsize = 'x-small')
##plt.grid()
##plt.autoscale(enable=True, axis='x', tight=True)
##plt.savefig('build/doppeleinzel.pdf')
##plt.clf()
#
##I_1 = I_1 * faktor
#
##m = np.zeros((112, 6))
##temp = np.zeros(112-s_1.size)
##s_1 = np.concatenate((s_1, temp))
##m[:,0] = np.zeros(112) + s_1*1e3
##temp = np.zeros(112-I_1.size)
##I_1 = np.concatenate((I_1, temp))
##m[:,1] = np.zeros(112) + I_1*1e9
##temp = np.zeros(112-s_2.size)
##s_2 = np.concatenate((s_2, temp))
##m[:,2] = np.zeros(112) + s_2*1e3
##temp = np.zeros(112-I_2.size)
##I_2 = np.concatenate((I_2, temp))
##m[:,3] = np.zeros(112) + I_2*1e9
##temp = np.zeros(112-s_3.size)
##s_3 = np.concatenate((s_3, temp))
##m[:,4] = np.zeros(112) + s_3*1e3
##temp = np.zeros(112-I_3.size)
##I_3 = np.concatenate((I_3, temp))
##m[:,5] = np.zeros(112) + I_3*1e9
##hr = ['$x_1/$mm', '$I_1/$nA', '$x_2/$mm', '$I_2/$nA', '$x_3/$mm', '$I_3/$nA']
##t = matrix2latex(m, headerRow=hr, format='%.2f')
#
