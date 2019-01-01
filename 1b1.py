# Fails : 1B1. py
# Autors : Egils Keišs
# Apliecibas numurs : 181REB314
# Datums : 01.01.2019
# Sagatave funkcijas saknes mekleeshanai ar dihatomijas metodi

# -*- coding : utf -8 -*-
import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
import numpy

from numpy import *      # Importē skaitlisko metožu bibliotēkas funkcijas
x = linspace(0, 7, 70)   # Trešais arguments ir ģenerējamo elementu skaits
y = cos(x)
y2 = sin(x)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $sin(x)*sin(x)$')
plt.plot(x, y, color = "#FF0000")
plt.plot(x,y2, color = "#007F00")
plt.show()
