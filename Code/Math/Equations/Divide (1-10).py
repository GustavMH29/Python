# Written by RF

while True:
    n=float(input("What number would you like to divide?"))
    q=(n/10)
    w=(n/9)
    e=(n/8)
    r=(n/7)
    t=(n/6)
    y=(n/5)
    u=(n/4)
    i=(n/3)
    o=(n/2)
    p=(n/1)
    print("This is", n, "divided by 1 to 10")
    print(n, "divided by 10", q)
    print(n, "divided by 9", w)
    print(n, "divided by 8", e)
    print(n, "divided by 7", r)
    print(n, "divided by 6", t)
    print(n, "divided by 5", y)
    print(n, "divided by 4", u)
    print(n, "divided by 3", i)
    print(n, "divided by 2", o)
    print(n, "divided by 1", p)
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
