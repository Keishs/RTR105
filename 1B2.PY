# Fails : 1B2. py
# Autors : Egils Keišs
# Apliecibas numurs : 181REB314
# Datums : 01.01.2019
# Sagatave funkcijas saknes mekleeshanai ar dihatomijas metodi

# -*- coding : utf -8 -*-
import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import *      # Importē skaitlisko metožu bibliotēkas funkcijas
x = linspace(0, 4, 11)   # Trešais arguments ir ģenerējamo elementu skaits
y = sin(x)


from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $sin(x)*sin(x)$')
plt.plot(x, y, color = "#FF0000")

y1 = x
plt.plot(x, y1, color = "#FFF000")

#var arī uzrakstīt tā ka dots y2 = x - x*x*x/(1*2*3)
y2 = y1 - x**3/(1*2*3)
plt.plot(x, y2, color = "#00FF00")

y3 = y2 + x**5/(1*2*3*4*5)
plt.plot(x, y3, color = "#00FFF0")

y4 = y3 - x**7/(1*2*3*4*5*6*7)
plt.plot(x, y4, color = "#0000FF")


plt.show()
