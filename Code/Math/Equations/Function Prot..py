# Written by RF

from pylab import *

    # Dette er funksjonen f(x) = x^2 + 2x (Df = [-5, 5]).
def f(x):
    return x**2 + 2*x

x_verdier = linspace(-5, 5, 100)
y_verdier = f(x_verdier)

plot(x_verdier, y_verdier)
show()
