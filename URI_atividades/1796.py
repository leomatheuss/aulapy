while True:
    case = int(input())
    lista = list(map(int,input().split(' ')))

    if (lista.count(1) > lista.count(0)) or (lista.count(1) == lista.count(0)):
        print('N')
    else:
        print('Y')
    
    break
