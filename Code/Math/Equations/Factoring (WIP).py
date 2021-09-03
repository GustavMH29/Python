# Written by RF

while True:
    # Python Program to find the factors of a number
    N=input("What number would you like to factor?")

    # This function computes the factor of the argument passed
    def print_factors(N):
        print("The factors of",N,"are:")
        for i in range(1, x + 1):
            if x % i == 0:
                print(i)
                      
    print_factors(N)
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
