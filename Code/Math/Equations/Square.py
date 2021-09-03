# Written by RF

while True:
    Q=float(input("What number would you like to square? "))
    H=float(input("How many times would you like to square it? "))
    S=((Q)**H)
    print("The", H, "square is", S)
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
