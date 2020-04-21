import math
while True:
    n = int(input())
    if n == 0: break
        matriz = []
        for i in range(1, n + 1):
            y = 1
            x = []
            if i <= math.ceil(n / 2):
                for j in range(n):
                    if y < i and j - 1 < n - i:
                        x.append(y)
                        y += 1
                    elif y == i and j - 1 < n - i:
                        x.append(y)
                    else:
                        y -= 1
                        x.append(y)
                matriz.append(x[:])
            else:
                matriz.append(matriz[n - i])
     
        for i in range(n):
            for j in range(n):
                if j < n - 1:
                    print('{:3}' .format(matriz[i][j]), end=' ')
                else:
                    print('{:3}' .format(matriz[i][j]))
        print()