# Fails : 191. py
# Autors :E
# Apliecibas numurs : 181REB314
# Datums : 03.12.2018
# Sagatave funkcijas saknes mekleeshanai ar dihatomijas metodi

# -*- coding : utf -8 -*-
from math import sin, cos, fabs
def f(x):
    return (1+(x**2))*sin(x)+(x*cos(x))
n=input('')
h=0.01
def f1(x):
    return(f(x+h)-f(x))/h
def f2(x):
    return(f1(x+h)-f1(x))/h
print '%g'%f1
print '%g'%f2
