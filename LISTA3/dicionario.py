dicionario = { 
        
        
        #chave  valor   #chave      valor       #chave   valor
        "nome": 'leo', "sobrenome": 'matheus', "conje": 'bruna'}


dic = {}
dic['nome'] = 'bruna'
dic['idade'] = 22
dic['sobrenome'] = 'reis'
dic['conje'] = 'leo'


#possivle solicitar o valor de uma chave com o dic['nome_da_chave']
dic.keys() # mostra as chaves
dicionario.values() #mostraosvalores
dic.items() #retorna uma lista de tuplas de chaves e valores
#para percorrer o dicionario e imprimir pdemos

for i in dicionario:
    print(i) #isso vai imprimir as chaves
    print(i, dicionario[i]) #isso vai impririmir as chaves e valor


