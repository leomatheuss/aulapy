salario = float(input())
round(salario, 2)

def calc_imposto(salario):
    if salario > 4500.00:
        imposto = (salario - 4500.00)*0.28 + 1500.00*0.18 + 1000*0.08
        print("R$ %.2f"% imposto)
    elif 3000.01 < salario <= 4500.00:
        imposto = (salario - 3000.00)*0.18 + 1000.00*0.08
        print("R$ %.2f"% imposto)
    elif 2000.01 < salario < 3000.00:
        imposto = (salario - 2000.01)*0.08
        print("R$ %.2f"% imposto)
    else:
        print("Isento")

calc_imposto(salario)
