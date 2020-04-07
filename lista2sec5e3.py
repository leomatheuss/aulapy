#notas válidas

nota1 = float(input())
nota2 = float(input())

if ((0.0 < nota1 < 10.0) and (0.0 < nota2 < 10.0)) == True:
    media = (nota1 + nota2 )/ 2
    print(f'A média das duas notas é {media}')
else:
    print("Uma, ou as duas notas estão inválidas")
