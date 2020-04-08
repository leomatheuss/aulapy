n = int(input("Entre com uma quantidade: "))

i = 0
contador = 0
maior = 0
qte_vez = 0
while i < n:
    x = int(input("Entre com um número: "))
    if x > maior:
        maior = x
        qte_vez = qte_vez + 1
    i = i + 1

print(f'O maior número é {maior} e foi lido {qte_vez} vezes')
