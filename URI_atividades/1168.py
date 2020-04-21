leds = (6,2,5,5,4,5,6,4,7,6)

n = int(input())

for i in range(n):
    num = input()
    soma = 0

    for j in num: 
        soma = soma + leds[int(j)]
    print(soma, "leds")