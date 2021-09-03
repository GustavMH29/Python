# Written by RF

import math

# Cube root and fourth root functionality are currently non-functional
# to fix in future

while True:
    
    n = float(input("What number would you like to derive the logarithm of? "))
    
    while True:
        answer = str(input("Is this a Common Logarithm? (y/n): "))
        if answer not in ('y', 'n'):
            print ("invalid input")
            continue      
        if answer == 'y':
            x = 10
            break
        else:
            x = 0
            break
    
    while True:
        if x == 10:
            break
        answer = str(input("Would you like to use Euler's number? (y/n): "))
        if answer not in ('y', 'n'):
            print("invalid input")
            break
        if answer == 'y':
            x = math.e
            break
        else:
            x = float(input("What base would you like to use? "))
            break
    
    srn = (math.sqrt(n))
    crn = (math.sqrt(srn))
    frn = (math.sqrt(crn))
    
    print("The normal is", math.log(n, x))
    print("The squared is", math.log(srn, x))
    print("The cubed is", math.log(crn, x))
    print("The fourth rooted is", math.log(frn, x))
    
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
