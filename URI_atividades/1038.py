valores = ["nda", 4.0,4.5,5.0,2.0,1.5]

a, b = input().split(' ')
a = int(a)
b = int(b)

pgto = valores[a] * b
print("Total: R$ {:.2f}".format(pgto))