import numpy as np
import math as m
import matplotlib.pyplot as plt

APhi = []
NPhi = []
T=[]
k = np.zeros(4)
q = np.zeros(4)


Amp = m.pi/3


phi=Amp
z=0
t=0

g=9.81
h=0.01
l=10


def ADSolve(t):
    return Amp*m.cos(m.sqrt(g/l)*t)

def f1(t,p,z):
    return z

def f2(t,p,z):
    return -(g/l)*m.sin(p)

while t < 20:
    APhi.append(ADSolve(t))
    NPhi.append(phi)
    T.append(t)
    k[0] = h * f1(t,phi,z) 
    q[0] = h * f2(t,phi,z)
    k[1] = h * f1(t+h/2,phi+k[0]/2,z+q[0]/2) 
    q[1] = h * f2(t+h/2,phi+k[0]/2,z+q[0]/2)
    k[2] = h * f1(t+h/2,phi+k[1]/2,z+q[1]/2)
    q[2] = h * f2(t+h/2,phi+k[1]/2,z+q[1]/2)
    k[3] = h * f1(t+h,phi+k[2],z+q[2]) 
    q[3] = h * f2(t+h,phi+k[2],z+q[2])
    phi = phi + (k[0]+2*k[1]+2*k[2]+k[3])/6
    z = z + (q[0]+2*q[1]+2*q[2]+q[3])/6
    t = t + h



plt.plot(T,NPhi,label='Аналитческое решение')
plt.plot(T,APhi,label='Численное решение')
plt.legend(loc=2)
plt.show()




