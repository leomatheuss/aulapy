def verifica(x, y):
    '''
    Função que vai verificar se o número é divisível por 13
    '''
    teste = 0
    for i in range(x, y+1):
        if i % 13 != 0:
            teste = teste + i
    print(teste)


a = int(input())
b = int(input())

if a < b:
    verifica(a, b)
elif a > b:
    verifica(b, a)
    