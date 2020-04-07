nota_lab = float(input("nota lab"))
nota_sem = float(input("nota av semestral"))
nota_exf = float(input("nota exame final"))

media = (nota_lab*0.2 + nota_sem*0.3 + nota_exf*0.5)
if (0 <= media <= 2.9):
    print("Aluno reprovado")
else:
    if (3.0 <= media <= 4.9):
        print("Recuperação")
    else:
        print("Aluno aprovado")

print(media)