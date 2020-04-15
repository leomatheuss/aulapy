numero = int(input())
lnum = len(str(numero))
aux = 0
temp = 0
soma = 0

while lnum > 0:
    aux = numero % 10
    soma = soma + aux
    temp = numero // 10
    numero = temp
    lnum = lnum - 1
    
print(soma)