# Fails : 181. py
# Autors : Egils Keišs
# Apliecibas numurs : 181REB314
# Datums : 03.12.18
# Sagatave funkcijas saknes mekleeshanai ar dihatomijas metodi
# -*- coding : utf -8 -*-
from math import cos, fabs
from time import sleep

def f1(x):
  return ((x*x)+x+1)/((cos(x)*cos(x)+0.1)



h=0
a = 0.; b = 6.2832
I1 = 0.
eps = 0.0001
I2 = (b-a) * ( f1(a) + f1(b) ) / 2

while (fabs(I2-I1)>eps):
  n=n*2
  h=(b-a)/n
  I1=I2
  I2=0
  k=0
  for k in range (0, n):
    I2=I2+h*f1(a+(k+0.5)*h)


print("a = %d, b =%d" %(a,b))
print ("Integrals:" ,I2)
print ("Iteraciju skaits:" ,k)

