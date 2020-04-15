import math

a = float(input("A"))
b = float(input("B)"))
c = float(input("C"))

delta = b**2 - (4*a*c)

resultado1 = 0
resultado2 = 0

if delta >= 0:
    resultado1 = (-b + math.sqrt(delta))/(2*a)
    resultado2 = (-b - math.sqrt(delta))/(2*a)
    if delta < 0:
        print("VALOR DE DELTA NEGATIVO")

print(resultado1)
print(resultado2)
    