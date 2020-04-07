altura = float(input("Entre com sua altura em m"))
sexo = str(input("Seu sexo, M para masculino e F para feminino"))

if sexo == 'M':
    peso_ideal = (72.7*altura) - 58
elif sexo == 'F':
    peso_ideal = (62.1*altura)-44.7

print("%2.f"% peso_ideal)   