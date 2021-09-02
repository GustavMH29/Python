from math import pi
while True:
  r=float(input("What is the radius in cm?"))
  f=((pi*3)+2)
  g=(f*r)
  print("The circumference is", g,"cm")
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