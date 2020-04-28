t = int(input())

dic = {}
for _ in range(t):
    i = int(input())
    if i in dic:
        dic[i] +=1
    else:
        dic[i] = 1

chaves = dic.keys() #valores que digitei em uma lista, mas sem repetir, vlore unicos
chaves = sorted(chaves)

for k in chaves:
    print("%d aparece %d vez(es)" %(k, dic[k]))
