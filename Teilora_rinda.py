# Fails : Teilora_rinda.py
# Autors : Egils Keišs
# Apliecibas numurs : 181REB314
# Datums : 02.01.2019


# -*- coding : utf -8 -*-

from math import sin

def manssin(x):
    k = 0
    a = (-1)**0*x**0/(1)
    S = a
    print("a0 = %6.2f S0 = %6.2f"%(a,S))

    while k < 500:
        k = k + 1
        R = (-1)*x*x/((2*k)*(2*k-1))
        a = a * R
        S = S + a
        if k == 499:
            print("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))

    print("a500 = %6.2f S500 = %6.2f"%(a,S))
    S = 1/2 + S/2
    return S

print("sin(x)*sin(x) aprekinasana:")
f = input("Ievadi argumentu (x): ")
x = float(f)
y = sin(x/2)
print("sin(x)*sin(x) = %6.2f"%(y))

yy = manssin(x/2)
print("sin(%.2f) = %6.2f"%(x,yy))

print("           100 ")
print("         -------- ")
print("         \                 k     4*k+2 ")
print("          \            (-1)   * x ")
print(" sin(0.24)= >       ---------------------- ")
print("          /                 (2*k+1)! ")
print("         / ")
print("         -------- ")
print("           k = 0 ")
print("                                    4 ")
print("                            (-1) * x ")
print(" Rekurences reizinātājs:  ----------------- ")
print("                            (4*k)*(4*k+1)")
