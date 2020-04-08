#a base do exercicio é essa, porem tentei fazer um pouco melhorado com opção, mas não deu certo


resposta = 'S'
i = 0
soma = 0
while resposta == 'S':
    codigo = int(input('Código do produto'))
    qtde = int(input('qtde produto'))
    
    if codigo == 100:
        total = 1.2*qtde
    elif codigo == 101:
        total = 1.3*qtde
    elif codigo == 102:
        total = 1.5*qtde
    elif codigo == 103:
        total = 1.2*qtde
    elif codigo == 104:
        total = 1.7*qtde
    elif codigo == 105:
        total = 2.2*qtde
    elif codigo == 106:
        total = 1.0*qtde
    
    i = i + 1 #contador
    soma = soma + total 
    print(f'O total do pedido até agora é de {soma}')
    resposta = str(input('Deseja Cadastrar mais produtos?[S/N]'))

    if resposta == 'N':
        print(f'O total final do pedido é de R$ {soma}')
        print(i)
        break
