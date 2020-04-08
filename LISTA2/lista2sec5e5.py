num = int(input())
soma = 0
if num < 0:
    print("Número inválido")
else:
    while num > 0:
        aux = num % 10 # pega o último numero
        num = num // 10 #devolve o novo numero sem o últomo
        soma = soma + aux #o ultimo número e coloca no somador

print(soma)
    
    