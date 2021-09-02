from math import pi
while True:
    D=float(input("What is the diameter in cm?"))
    O=(pi*D)
    print("The circumference is", O, "cm")
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
