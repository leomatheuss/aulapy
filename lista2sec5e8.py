print("Esscolha a opção")
print("1 - Soma de dois números")
print("2 - DIferença entre dois números")
print("3 - Produto entre dois números")
print("4 - Divisão entre dois números")

escolha = int(input())

if escolha == 1:
    num1 = int(input("Número1"))
    num2 = int(input("Número2"))
    soma = num1 + num2
    print(soma)
else:
    if escolha == 2:
        num1 = int(input("Número1"))
        num2 = int(input("Número2"))
        dif = num1 - num2
        print(dif)
    else:
        if escolha == 3:
            num1 = int(input("Número1"))
            num2 = int(input("Número2"))
            prod = num1 * num2
            print(prod)

        else: 
            if escolha == 4:
                num1 = int(input("Número1"))
                num2 = int(input("Número2"))
                div = num1/num2
                print(div)
            else:
                print("ESCOLHA INVÁLIDA")