# Written  by RF

while True:
  answer = input("Value now =")
  value = float(answer)
  answer = input("Valuechange in percent =")
  percent = float(answer)
  growthfactor = 1 + percent/100
  year = 0
  while year < 5:
    year = year + 1
    value = value*growthfactor
  print("After", year, "year(s), the value is", int(value),"$")
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
