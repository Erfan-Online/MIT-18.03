from math import sin

def y_prime(x):
    return 4/(1+x**2)

x, y = 0, 0
h = 0.01

while x < 1:
    y += y_prime(x)*h
    x += h

print("{:6.3f} {:6.3f}".format(x, y))

def p_prime(p):
    return 0.05*p - 0.002*p**2

h = 1
t, p = 0, 3

while t <= 10 * 12:
    p += p_prime(p)*h
    t += h

print("{:6.3f} {:6.3f}".format(t, p))


def f(y, t):
    return y * sin(t)

h = 0.2
t, y = -3, 1

while t <= 2:
    y += f(y, t)*h
    t += h

print("{:6.3f} {:6.3f}".format(t, y)) 

print(f"error: {(0.54 - y) / h}")