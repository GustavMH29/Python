# Written by RF

import math

a = float(input("a = "))
T = float(input("T = "))
B = float(input("B = "))
aT = (a/T)
aTB = (aT+B)
print("aTB = ", aTB)
print("R = ", math.log(aTB, 10))
