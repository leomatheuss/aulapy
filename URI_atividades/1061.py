reajuste = [0.15, 0.12, 0.1, 0.07, 0.04]
salario = float(input())

novo_sal = 0
if salario <= 400:
    novo_sal = salario * reajuste[0] + salario
    print("Novo salario: {:.2f}".format(novo_sal))
    print("Reajuste ganho: {:.2f}".format(salario*reajuste[0]))
    print("Em percentual: 15 %")
elif 400.01 <= salario <= 800.00:
    novo_sal = salario * reajuste[1] + salario
    print("Novo salario: {:.2f}".format(novo_sal))
    print("Reajuste ganho: {:.2f}".format(salario*reajuste[1]))
    print("Em percentual: 12 %")
elif 800.01 <= salario <= 1200.00:
    novo_sal = salario * reajuste[2] + salario
    print("Novo salario: {:.2f}".format(novo_sal))
    print("Reajuste ganho: {:.2f}".format(salario*reajuste[2]))
    print("Em percentual: 10 %")
elif 1200.01 <= salario <= 2000.00:
    novo_sal = salario * reajuste[3] + salario
    print("Novo salario: {:.2f}".format(novo_sal))
    print("Reajuste ganho: {:.2f}".format(salario*reajuste[3]))
    print("Em percentual: 7 %")
elif salario > 2000.00:
    novo_sal = salario * reajuste[4] + salario
    print("Novo salario: {:.2f}".format(novo_sal))
    print("Reajuste ganho: {:.2f}".format(salario*reajuste[4]))
    print("Em percentual: 4 %")

