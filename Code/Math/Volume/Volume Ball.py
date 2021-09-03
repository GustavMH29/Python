# Written by RF

from math import pi
while True:
    D=float(input("What is the diameter in cm?"))
    r=(D/2)
    pif=(pi*4)
    A=(pif*r**2)
    V=((1/3)*A*r)
    print("The volume is", V, "cm^3")
    while True:
        answer = str(input('Anything else? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Godspeed")
        break
