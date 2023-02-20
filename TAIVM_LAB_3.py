import math

F = lambda x: math.tan(x**2+0.3) + 2
dF = lambda x: 2*x*(math.tan(x**2+0.3)**2 + 1)
eps = 0.0001

n = 0
a = 1
b = 1.5
while True:
    n += 1
    c = (b + a)/2
    F_c = F(c)
    if b - a < 2*eps:
        break
    if(F_c == 0):
        break
    if((F(a) < 0.0) & (F_c > 0.0)):
        b = c
    else:
        a = c
print(c, ";   ", F(c), ";   ", n)

n = 0
a = 1.5
c = 1
while True:
    n += 1
    c_p = c
    F_a = F(a)
    F_b = F(c_p)
    c = a - ((c_p - a)/(F_b - F_a) * F_a)
    if abs(c - c_p) < eps:
        break
print(c, ";   ", F(c), ";   ", n)

n = 0
c = 1.5
while True:
    n += 1
    c_p = c
    c = c_p - F(c_p)/dF(c_p)
    if abs(c - c_p) < eps:
        break
print(c, ";   ", F(c), ";   ", n)

n = 0
t = 0.1
c = 1.5
while True:
    n += 1
    c_p = c
    c = c_p - t*F(c_p)
    if abs(c - c_p) < eps:
        break
print(c, ";   ", F(c), ";   ", n)
