valores = []

while len(valores) < 5:
    valores.append(int(input()))

par = 0
impar = 0
negativo = 0
positivo = 0

for i in valores:
    if (i % 2) == 0:
        par = par + 1
    elif i % 2 != 0:
        impar = impar + 1
    if i > 0:
        positivo = positivo + 1
    elif i < 0:
        negativo = negativo +1
    
print(par,'valor(es) par(es)')
print(impar, 'valor(es) impar(es)')
print(positivo, 'valor(es) positivo(s)')
print(negativo,'valor(es) negativo(s)')