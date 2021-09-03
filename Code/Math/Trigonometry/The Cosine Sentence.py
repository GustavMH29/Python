# Written by RF

from math import sqrt
from math import cos
while True:
  # Explanations
  print("This is meant to calculate side BC in a non-right triangle,")
  print("where corner A is to the left, B is right, corner C is the peak,")
  print("and we have a point D severing it into two right triangles.")
  print("And this sentence applies; DB = AB - AD.")
  print(" ")
  
  # Gathering of values
  AB=float(input("What is the length of side AB?"))
  AD=float(input("What is the length of side AD?"))
  CD=float(input("What is the length of side CD?"))
  v=float(input("What is the value of angle A?"))
  print(" ")
  
  # Calculations of BC
  Cv=(cos(v))
  print("The cosine of v is", Cv)
  AC2=(AD**2)+(CD**2)
  AC=(sqrt(AC2))
  BC2=(AD**2)+(AC2)-(2*AB*AD)
  BC=(sqrt(BC2))
  print("The length of BC is", BC)
  print(" ")

  # Usage of the Cosine sentence
  while True:
    print("The Cosine sentence goes as follows;")
    print("a^2 = b^2 + c^2 - 2 * b * v * cos v")
    print("In this case BC = a, AC = b, AB = c and angle A = v.")
    a=(BC)
    b=(AC)
    c=(AB)
    if(AD!=AC*(cos(v))):
      print("These values do not operate")
      break
    else:
      continue
    Cs=(b**2)+(c**2)-(2*b*c)*(cos(v))
    print("The Cosine sentence gives us", Cs)
    if(Cs==BC):
      print("The Cosine sentence is now proven")
      continue
    else:
      print("These values do not operate")
      break
    
  # Program restart 
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
