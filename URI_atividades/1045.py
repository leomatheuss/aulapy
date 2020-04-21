a, b, c = input().split(' ')
a = float(a)
b = float(b)
c = float(c)
lista = [a, b, c]
lista.sort()
lista = lista[::-1]
a, b, c = lista


if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:  
    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")
    if a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
    if a**2 < b**2 + c**2:
        print("TRIANGULO ACUTANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    if (a == b and b != c and a !=c) or (a == c and c != b and a !=b) or (b == c and a !=c and a != b):
        print("TRIANGULO ISOSCELES")