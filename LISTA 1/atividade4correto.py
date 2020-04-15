aposta = 5.0

ap1 = float(input())
ap2 = float(input())
ap3 = float(input())

premio = int(input("Quanto foi o prêmio total"))

total_ap = ap1 + ap2 + ap3

if total_ap < aposta:
    print("Valor não corresponde a aposta")
else:
    if total_ap > aposta:
        resto = total_ap - aposta
        total_ap = total_ap - resto 
        x1 = 20*ap1
        x2 = 20*ap2
        x3 = 20*ap3

        print(f'O apostador 1 ganhou {x1}% do prêmio')
        print(f'O apostador 2 ganhou {x2}% do prêmio')
        print(f'O apostador 3 ganhou {x3}% do prêmio')

x1 = 20*ap1
x2 = 20*ap2
x3 = 20*ap3

print(f'O apostador 1 ganhou {x1}% do prêmio')
print(f'O apostador 2 ganhou {x2}% do prêmio')
print(f'O apostador 3 ganhou {x3}% do prêmio')



