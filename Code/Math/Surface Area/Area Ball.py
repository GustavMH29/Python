# Written by RF

from math import pi
while True:
    D=float(input("What is the diameter in cm?"))
    r=(D/2)
    pif=(pi*4)
    A=(pif*r**2)
    print("The area is", A, "cm^2")
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
