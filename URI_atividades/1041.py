def verifica_quadrante(a,b):
    if a > 0 and b > 0:
        return(print("Q1"))
    elif a > 0 and b < 0:
        return(print("Q4"))
    elif b > 0 and a < 0:
        return(print("Q2"))
    elif b < 0 and a < 0:
        return(print("Q3"))


x, y = input().split(' ')
x = float(x)
y = float(y)

verifica_quadrante(x, y)

if x == y == 0:
    print("Origem")
if x == 0 and y != 0:
    print("Eixo Y")
elif y == 0 and x != 0:
    print("Eixo X")



