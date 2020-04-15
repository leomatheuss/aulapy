type([])

lista1 = [1,2,3,4,5, 99, 4, 21, 12, 0, 2, 2, 88]

#nomedalista.sort() ordena a lista em ordem crescente



lista2 = ['L', 'E', 'O', '', 'M', 'A', 'T', 'H']
# se o sort for utilizado com listas de strings, como essa, ele usa ordem alfabética, pero antes os espaços e caracteres eespeciais



lista3 = []

lista4 = list(range(11))


lista5 = list('Leonardo Matheus')

print(lista5)
print(lista4)

#check de valor contido na lista, serve também para prourar strings em listas de strings	

if 81 in lista4:
	print('há um número 8')
else:
	print('não tá')

################## 

#podemos contar o numero de ocorrências de um valor na lista, sem usar for ou nada

print(lista1.count(4))
print(lista5.count('e'))

#add elementos em lista
#obs: p/ adicionar os elementos ou valores, utilizamos append.

lista1.append(42) #com append podemos passar apenas um elemento

#mas podemos inserir mais de um elemento, como uma lista, ou seja, lista dentro de lista

lista1.append([4,5,6]) #nesse caso ele adiciona a lista dentro da lista


lista1.extend([123, 44, 47]) #com o extend ele adiciona os valores da lista, dentro da outra lista, sem a lista ficar adicionada

#para inserir um valor em determinada posição da lista
#utilizar a função .insert(POSIÇÃO, VALOR)
#isso não substitui outro valor, apenas colca no local e o ex-valor é deslocado pra posição à direita.
lista1.insert(2, 'NOVO VALOR')

## FUNÇÃO .SORT() ordena a lista

lista6 = lista1 + lista2 #soma listas em uma nova

lista2.reverse() #inverte a lista

# é a mesma coisa que fazer o slice

lista2[::-1]

#copiar uma lista

lista7 = lista2.copy()

len(lista1)

#podeos remover o último elemento de uma lista
# o .pop remove E retorna esse elemento
#para remover um valor de algum indice, numerar dentro do ()

#além disso, se o eleento NÃO for em uma das pontas,  ele desloca para esquerda
lista7.pop()

nome = 'Leonardo Canjica Matheus'
#pega uma string e divide as frases em um vetor
nome = nome.split()
#quando o slit() estiver sem parâmetro, ele separa a string de acordo com o espaço
#para escolher um separador diferente, basta adcionnar entre os parenteses
#exemplo nome = Leonardo-Matheus-Canjica
#nome.split('-') nesse caso o separador é o hífen



#lista.clear() limpa a lixta

#para converter uma lista em uma string basta
#lista = ''.join(lista6)

lista8 = ''.join(lista2)

curso = 'ProgramaçãoPython:Essencial'

#isso vai fazer com que todo espaço seja substituido por $
nome = '$'.join(nome)

#é possível iterar sobre listas
#utilizando for:

for elemento in lista4:
	print(elemento)

#utilizando while

carrinho = []
produto = ''

while produto != 'sair':
	print("add produto")
	produto = str(input()
	if produto != 'sair':
		carrinho.append(produto)
for produto in carrinho:
	print(produto)


#######################################
# possível utilizar variáveis em listas 

# é possível gerar o indice com um for, para organização
#          0		1			2		3
cores = ['verde', 'amarelo', 'azul', 'branco']

for indice, cor in enumerate(cores):
	print(indice, cor)


#ALGUMAS FUNCIONALIDADES DE LISTAS

#encontrar o índice em uma lista

numbers = [1, 5, 3, 4, 5, 6, 8,9, 10]

#em qual indice está o valor
numbers.index('valor que você quer descobrir o index')
#exemplo
#nesse caso, se o numero for repetido,ele retorna o primeiro encontrado
numbers.index(5)

#podemosfazer busca denetro deum range,ou seja,qual indice começar a buscar

numbers.index(5,2)

#revisando slice
#lista[inicio,fim, passp]

#slices de listas

lista44 = [1,2,3,4]
print(lista44[1::])

#com parametro fim

#lista.reverse() inverte a lista

#desempacotamento de lista

#num1, num2, num3, num4 = lista44

#desempacota apenas com n de variáveis igual ao n de indices da lista

#copiando uma lista para outra (shallowcopy e deepcopy)

lista55 = [1,2,3,4,5,6]
newlist = lista55.copy
print(newlist)

newlist.append(4)

