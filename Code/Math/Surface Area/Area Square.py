# Written by RF

while True:
    s1=float(input("What is the length of side one in cm?"))
    s2=float(input("What is the length of side two in cm?"))
    A=(s1*s2)
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
