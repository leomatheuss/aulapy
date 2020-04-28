def verifica_quad(a, b):
    if a > 0 and b > 0:
        return(print("primeiro"))
    elif a > 0 and b < 0:
        return(print("quarto"))
    elif b > 0 and a < 0:
        return(print("segundo"))
    elif b < 0 and a < 0:
        return(print("terceiro"))

while True:

    x, y =  map(int,input().split())
    if x == 0 or y == 0:
        break
    else:
        verifica_quad(x,y)