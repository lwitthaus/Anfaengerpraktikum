import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *

#R_2 = ufloat(500, 1)
#R_v = ufloat(321/679, 321/679*0.005)
#R_x = R_2 * R_v
#print(R_x)
#
#R_q = ufloat(1000, 2)
#R_w = ufloat(190/810, 190/810*0.005)
#R_y = R_q * R_w
#print(R_y)
#
#R_e = ufloat(332, 1)
#R_r = ufloat(417/583, 417/583*0.005)
#R_z = R_e * R_r
#print(R_z)
#
#
#a = np.std([236.5, 232.0, 237.4])
#print(a)

#zweiter Widerstand, Wert 12
#R_2 = ufloat(500, 1)
#R_v = ufloat(428/572, 428/572*0.005)
#R_x = R_2 * R_v
#print(R_x)
#
#R_q = ufloat(1000, 2)
#R_w = ufloat(263/737, 263/737*0.005)
#R_y = R_q * R_w
#print(R_y)
#R_e = ufloat(332, 1)
#R_r = ufloat(530/470, 530/470*0.005)
#R_z = R_e * R_r
#print(R_z)
#
#a = np.std([374.0, 357.0, 374.5])
#print(a)




#Kapazität Wert 1
#C_q = ufloat(992*10**(-9), 2*10**(-9))
#R_q = ufloat(400/600, 400/600*0.005)
#C_1 = C_q * R_q
#print(C_1)
#
#
#C_w = ufloat(597*10**(-9), 1*10**(-9))
#R_w = ufloat(526/474, 526/474*0.005)
#C_2 = C_w * R_w
#print(C_2)
#
#C_e = ufloat(399*10**(-9), 1*10**(-9))
#R_e = ufloat(624/376, 624/376*0.005)
#C_3 = C_e * R_e
#print(C_3)

#a = np.std([6.62, 6.63, 6.62])
#print(a)




#Kapazität Wert 3
#C_e = ufloat(399*10**(-9), 1*10**(-9))
#R_e = ufloat(1.053,0.005)
#C_1 = C_e * R_e
#print(C_1)
#C_w = ufloat(597*10**(-9), 1*10**(-9))
#R_w = ufloat(413/587, 413/587*0.005)
#C_2 = C_w * R_w
#print(C_2)
#C_q = ufloat(992*10**(-9), 2*10**(-9))
#R_q = ufloat(297/703, 297/703*0.005)
#C_3 = C_q * R_q
#print(C_3)

#a= np.std([4.201, 4.203, 4.186])
#print(a)




#Kapazität (Wert 8)
#C_q = ufloat(992*10**(-9), 2*10**(-9))
#R_q = ufloat(229/771, 229/771*0.005)
#C_1 = C_q * R_q
#R_a = ufloat(170, 5.1)
#print(C_1)
#
#C_w = ufloat(597*10**(-9), 1*10**(-9))
#R_w = ufloat(329/671, 329/671*0.005)
#C_2 = C_w * R_w
#print(C_2)
#
#C_e = ufloat(399*10**(-9), 1*10**(-9))
#R_e = ufloat(424/576, 424/576*0.005)
#C_3 = C_e * R_e
#print(C_3)

#a = np.std([2.946, 2.925, 2.937])
#print(a)


#R_a = ufloat(170, 5.1)
#R_q = ufloat(771/229, 771/229*0.005)
#R_1 = R_a * R_q
#print(R_1)
#print(R_1.s)
#R_b = ufloat(281, 8.43)
#R_w = ufloat(671/329, 671/329*0.005)
#R_2 = R_b * R_w
#print(R_2)
#print(R_2.s)
#R_c = ufloat(422, 12.66)
#R_e = ufloat(576/424, 576/424*0.005)
#R_3 = R_c * R_e
#print(R_3)
#print(R_3.s)

#a = np.std([667, 673, 673])
#print(a)




#Induktivität Wert 17
#L_q = ufloat(27.5*10**(-3), 0.06*10**(-3))
#R_q = ufloat(607/393, 607/393*0.005)
#L_1 = L_q * R_q
#print(L_1)
#
#L_w = ufloat(20.1*10**(-3), 0.04*10**(-3))
#R_w = ufloat(91/909, 91/909*0.005)
#L_2 = L_w * R_w
#print(L_2)
#
#L_e = ufloat(14.6*10**(-3), 0.03*10**(-3))
#R_e = ufloat(99/901, 99/901*0.005)
#L_3 = L_e * R_e
#print(L_3)
#a = np.std([42.49, 2.01, 1.61])
#print(a)


R_a = ufloat(61, 1.83)
R_q = ufloat(607/393, 607/393*0.005)
R_1 = R_a * R_q
print(R_1)

R_b = ufloat(1000, 30)
R_w = ufloat(91/909, 0.001)
R_2 = R_b * R_w
print(R_2)

R_c = ufloat(1000, 30)
R_e = ufloat(99/901, 0.001)
R_3 = R_c * R_e
print(R_3)
#a = np.std([94.2, 100.0, 110.0])
#print(a)





#Induktivität Maxwell Brücke
#C = ufloat(597*10**(-9), 1*10**(-9))
#R_a = ufloat(332, 1)
#R_q = ufloat(203, 6.09)
#L_1 = R_a * R_q * C
#print(L_1)
#
#R_b = ufloat(500, 1)
#R_w = ufloat(139, 4.17)
#L_2 = R_b * R_w * C
#print(L_2)
#
#R_c = ufloat(1000, 2)
#R_e = ufloat(68, 2.04)
#L_3 = R_c * R_e * C
#print(L_3)

#a = np.std([40.2, 41.5, 40.6])
#print(a)


#R_d = ufloat(715, 21.45)
#
#R_1 = R_a * R_q /R_d
#print(R_1)
#print(R_1.s)
#
#R_2 = R_b * R_w / R_d
#print(R_2)
#print(R_2.s)
#
#R_3 = R_c * R_e /R_d
#print(R_3)
#print(R_3.s)
#a = np.std([94, 97, 95])
#print(a)
