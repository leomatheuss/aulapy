t = int(input())
numeros = []
num = []
for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        numeros.append(n)
    else:
        num.append(n) 

numeros.sort()
num.sort(reverse=True)

numeros.extend(num)
for i in numeros:
    print(i)