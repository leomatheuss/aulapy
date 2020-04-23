nome = str(input())
salario = float(input())
vendasdinheiro = float(input())

COMISSAO = 0.15

sal_final = salario + vendasdinheiro*COMISSAO

print("TOTAL = R$ %.2f"% sal_final)