a, b = input().split(" ")
inicio = int(a)
fim = int(b)

if inicio == fim:
    print("O JOGO DUROU 24 HORA(S)")
else:
    tempo_total = fim - inicio
    if tempo_total < 0:
        tempo_total += 24
    print("O JOGO DUROU %d HORA(S)" %tempo_total)