# Written by RF

from math import sqrt
while True:
  print("We are to solve the quadratic equation: ax^2 + bx + c = 0")
  answer = input("a =")
  a = float(answer)
  if a == 0:
    print("This is no quadradic equation")
  else:
    answer = input("b =")
    b = float(answer)
    answer = input("c =")
    c = float(answer)
    d = b**2-(4*a*c)
    if d < 0:
      print("No answer")
    elif d == 0:
      x1 = -b/(2*a)
      print("An answer, x =", round(x1,2))
    else:
      x1 = (-b+sqrt(d))/(2*a)
      x2 = (-b-sqrt(d))/(2*a)
      print("Two answers, x =", round(x1,2), "og x =", round(x2,2))
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
