# Written by RF

while True:
    import math
    n = float(input("What number would you like to derive the logarithm of?"))
    x = float(input("What base would you like to use?"))
    print(math.log(n, x))
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
