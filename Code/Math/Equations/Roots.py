# Written by RF

from math import sqrt
while True:
    Q=float(input("What number would you like to root?"))
    R=(sqrt(Q))
    print("The square root is", R)
    C=(sqrt(R))
    print("The cube root is", C)
    F=(sqrt(C))
    print("The fourth root is", F)
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

