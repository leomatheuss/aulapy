valor = int(input())
v_lido = valor

notas = [100, 50, 20, 10, 5, 2, 1] 

dict_notas = {}
for i in notas:
    dict_notas[i] = valor //  i
    valor -= dict_notas[i] * i

print(v_lido)
for i in dict_notas:
    print(dict_notas[i],' nota(s) de R$ ',i,',00',sep='')