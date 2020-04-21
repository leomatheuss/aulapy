par = []
impar = []

cont = 0
while cont < 15:
    n = int(input())
    if n % 2 == 0:
        par.append(n)
        if len(par) == 5:
            for i, pares in enumerate(par):
                print("par[",i,"] = ", pares,sep='')
            par.clear()
    else:
        impar.append(n)
        if len(impar) ==5:
            for i, impares in enumerate(impar):
                print("impar[",i,"] = ", impares,sep='')
            impar.clear()
    
    cont += 1
for i, impares in enumerate(impar):    
    print("impar[",i,"] = ", impares,sep='')
for i, pares in enumerate(par):
    print("par[",i,"] = ", pares,sep='')
    