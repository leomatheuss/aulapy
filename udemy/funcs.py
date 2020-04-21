'''
Definindo funções


* Funções são pequenos trechos de código que realizam
  tarefas expecificas.

* Já utilizamos várias funções:
	print()
	len()
	max()
	min()
'''


# Exemplos #

cores = ['verde','amarelo','azul','branco']

#Utilizando uma função integrada do python (built-in))

n = 1
while len(cores) < 15:
	for i in cores:
		cor = str(input())
		cores.append(cor)
