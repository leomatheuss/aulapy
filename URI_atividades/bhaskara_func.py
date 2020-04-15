import math
from decimal import Decimal


a,b,c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)

delta = (b**2 -4*a*c)
delta = round(delta, 4)
div = 2 * a
if a == 0 or delta < 0:
    print("Impossível Cálcular")
else:
    R1 = (-b + math.sqrt(delta)) / div 
    R2 = (-b - math.sqrt(delta))/ div



print("R1 = %.5f"% R1)
print("R2 = %.5f"% R2)