num = int(input("Número inteiro"))
strnum = str(num)


if len(strnum) != 3:
    print("Você entrou com um número com mais de 3 digitos")
else:
    print(str(num))
    
    print(strnum[::-1])