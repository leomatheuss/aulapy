def mdc(x,y):
    '''
    algoritmo de euclides
    '''
    anterior = x
    atual = y
    resto = anterior % atual
    while resto != 0:
        anterior = atual
        atual = resto
        resto = anterior % atual
    
    return print(atual)



teste = int(input())
cont = 0

while cont < teste:
    f1, f2 = input().split(' ')
    f1 = int(f1)
    f2 = int(f2)
    mdc(f1,f2)

    cont += 1