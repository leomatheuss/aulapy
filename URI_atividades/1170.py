def blobs(x):
    total_comida = x
    dias = 0
    while total_comida > 1:
        total_comida = total_comida/2
        dias += 1
    return print(dias,"dias")


teste = int(input())
cont = 0
while cont < teste:
    a = float(input())
    blobs(a)
    cont += 1
