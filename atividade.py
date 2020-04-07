total = float(input())

total_desc = total*0.9
parc = total/3
comissao_av = total_desc*0.05
comissao = total*0.05

print(f'O total com desconto é R${total_desc}')
print(f'O valor de cada parcela, no parcelamento 3x é de R${parc}')
print(f'Comissão caso venda à vista R${comissao_av}')
print(f'Comissão caso venda à prazo R${comissao}')

