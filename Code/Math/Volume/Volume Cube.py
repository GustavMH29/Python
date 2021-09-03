# Written by RF

while True:
    L=float(input("What is the length in cm?"))
    B=float(input("What is the width in cm?"))
    h=float(input("What is the height in cm?"))
    V=(L*B*h)
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
