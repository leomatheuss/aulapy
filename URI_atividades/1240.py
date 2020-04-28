t = int(input())

for _ in range(t):
    x = input().split()
    A, B = x[0], x[1]
    tA = len(A)
    tB = len(B)
    if tA >= tB:

        if A[tA-tB:tA] == B:
            print('encaixa')
        else:
            print('nao encaixa')

    else:
        print('nao encaixa')