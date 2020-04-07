import random
import os
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
contador = 0
acerto = 0
while contador < 5:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(f'Qual a soma de {num1} + {num2}')
    soma = num1 + num2
    somateste = int(input())

    if soma == somateste:
        print("Parabéns, você acertou")
        acerto = acerto + 1
    else:
        print(f'Você errou, a resposta correta seria: {soma}')
    contador = contador + 1
os.system('clear')

print(f'Você acertou {acerto} respostas')