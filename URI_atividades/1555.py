teste = int(input())

for _ in range(teste):
    x, y = input().split(' ')
    x = int(x)
    y = int(y)
    r = (3*x)**2 + y**2
    b = 2*(x**2)+ (5*y)**2
    c = -100*x + y**3

    maior = r
    if b > maior and b > c:
        maior = b
        print("Beto ganhou")
    elif c > maior and c > r:
        maior = c
        print("Carlos ganhou")
    else:
        print("Rafael ganhou")