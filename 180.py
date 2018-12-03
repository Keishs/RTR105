from math import cos,fabs
def f1(x):
    return ((x*x)+x+1/(cos(x)*cos(x)+0.1)
    a=0;b=6.2832;I1=0.;n=1
    eps=0.001
    I2=(b-a)*(f1(a)+f1(b))/2
while (fabs(I2-I1)>eps):
    n=n*2
    h=(b-a)/n
    I1=I2
    I2=0
    for k in range(n):
        I2=I2+h*f1(a+(k+0.5)*h)
print " Integrālis ir" ,I2
