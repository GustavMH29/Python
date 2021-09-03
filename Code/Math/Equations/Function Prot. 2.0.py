# Written by RF

from pylab import *

def f(x):
    return x**2 + 2*x

x_verdier = linspace(-5, 5, 100)
y_verdier = f(x_verdier)

xlabel("x")                     # Aksetittel langs x-aksen
ylabel("f(x)")                  # Aksetittel langs y-aksen
axhline(y=0, color="black")     # Legger til en x-akse
axvline(x=0, color="black")     # Legger til en y-akse
grid()                          # Legger til et rutenett

plot(x_verdier, y_verdier)
show()
