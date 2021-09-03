# Written by RF

from math import sqrt
while True:
    k1=float(input("What is the length of Katet 1 in cm?"))
    k2=float(input("What is the length of Katet 2 in cm?"))
    h=sqrt(k1**2+k2**2)
    print("The hypotenuse is", h, "cm")
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

