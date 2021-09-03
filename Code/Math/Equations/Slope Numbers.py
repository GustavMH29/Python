# Written by RF

while True:
    x1=float(input("What is the x coordinate of the first point?"))
    y1=float(input("What is the y coordinate of the first point?"))
    x2=float(input("What is the x coordinate of the second point?"))
    y2=float(input("What is the y coordinate of the second point?"))
    x=(x1-x2)
    y=(y1-y2)
    a=(y/x)
    print("The slope number is", a)
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

