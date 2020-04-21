n_testes = int(input())

for i in range(n_testes):
    pA, pB, g1, g2 = input().split(' ')
    pA = int(pA)
    pB = int(pB)
    g1 = float(g1)
    g2 = float(g2)

    anos = 0
    while pA <= pB:
        count_pa = int((pA*(g1/100)))
        count_pb = int((pB*(g2/100)))

        anos = anos + 1
        pA = pA + count_pa
        pB = pB + count_pb

        if anos > 100:
            break
    if anos > 100:
        print("Mais de 1 seculo")
    else:
        print("%d anos." %anos)