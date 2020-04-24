while True:
    qte = int(input())

    if qte == 0:
        break

    resultados = list(map(int,input().split(' ')))
    maria = 0
    joao = 0

    for i in resultados:
        if i == 0:
            maria = maria + 1
        else:
            joao = joao + 1
    
    print("Mary won %d times and John won %d times" %(maria,joao))

