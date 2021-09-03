# Written by RF

while True:
    print("This program is to derive a standard quadratic equation.")
    print("f(x) = ax^2 + bx + c")
    a = input("What is the constant 'a'?")
    b = input("What is the constant 'b'?")
    c = input("What is the constant 'c'?")
    product = (a*2)
    print("f(x)", a + "x^2 +", b + "x +", c)
    print("f'(x) =", product + "x +", b)
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
