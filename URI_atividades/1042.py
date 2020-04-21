a,b,c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

valores = [a,b,c]
sort_valores = valores.copy()
sort_valores.sort()

for i in sort_valores:
    print(i)
print("")
print("")
for i in valores:
    print(i)
    