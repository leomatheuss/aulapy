import math

while True:
    try:
        a, b = input().split(' ')
        a = int(a)
        b = int(b)
        soma_fat = math.factorial(a) + math.factorial(b)
        print(soma_fat)
    except:
        break
