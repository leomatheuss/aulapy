
a = int(input())
b = int(input())
nao_eh = 0

if a < b:
    for i in range(a, b + 1):
        if i % 13 != 0:
            nao_eh = nao_eh + i
elif a > b:
    for i in range(b, a+1):
        if i % 13 !=0:
            nao_eh = nao_eh + i
    

print(nao_eh)
    