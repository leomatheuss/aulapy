lista1 = list(map(int,input().split(' ')))
lista2 = list(map(int,input().split(' ')))

i = 0

for n in range(3):
    j = lista2[n] - lista1[n]   
    if j > 0:
        i = i + j
print(i)