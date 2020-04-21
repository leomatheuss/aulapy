carrinho = []
produto = ''

while produto != 'sair':
    print("Add produto na lista")
    produto = str(input())
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
    
print(carrinho)