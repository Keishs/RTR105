# Fails : 170. py
# Autors : Egils Keišs
# Apliecibas numurs : 181REB314
# Datums : 03.12.2018
# Sagatave funkcijas saknes mekleeshanai ar dihatomijas metodi

# -*- coding : utf -8 -*-
from math import fabs,sinh,cos
from time import sleep
def f(x):
    return (-1)*cos(a*x)*(3.14/8)+(2*cos(3*a*x)/(3*3.14))-(2*cos(5*a*x)/(5*3.14))x*x*sinh(x)+cos(x)
a=1

funa = f(a)
funb = f(b)
if(funa*funb>0.0 ):
    print "Dotajā intervālā [%s, %s] sakņu nav"%(a,b)
    sleep(1);exit()
else :
    print "Dotajaa intervaalaa sakne (s) ir!"
    deltax = 0.0001
    while ( fabs(b-a)>deltax ):
        x = (a+b )/2;funx=f(x)
        if (f(x)==0):
            print "trāpījums tieši saknē"
            
        else:
            if(funa*funx<0.):
                b=x
            else:
                a=x
                
    print "Sakne ir:", x,f(x)
