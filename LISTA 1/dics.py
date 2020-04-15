'''
PARA ACESSAR UM DICIONAEIO:

DICNOME.GET(CHAVE)


#metodos de dicionários

'''

dicionario = {'a': 1, 'b': 2, 'c': 3}

#limpar dicionario

dicionario.clear()

#copiando um dict para outro

#deep copy
novo = dicionario.copy()
novo['d'] = 4

#shallow copy

novo = dicionario
novo['e'] = 5


#criação não usual de dicionario

outro = {}.fromkeys('a','b')

#o metodo fromkeys recebe dois parâmetros, um iteravel e um valor, ele vai gerar para cada valor do iteravel
#uma chave e irá atribuir a esta chave o valor informado

usuario = {}.fromkeys(['noem', 'pontos', 'email', 'profile'], 'desconhecido')


