# Written by RF

while True:
    G=float(input("What is the baselength in cm?"))
    h=float(input("What is the height in cm?"))
    A=(G*h)
    A2=(A/2)
    print("The area is", A2, "cm^2")
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
