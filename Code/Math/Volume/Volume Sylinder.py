# Written by RF

from math import pi
while True:
    D=float(input("What is the diameter in cm?"))
    r=(D/2)
    G=(r**2*pi)
    print("The base is", G, "cm^2")
    h=float(input("What is the height in cm"))
    V=(G*h)
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
