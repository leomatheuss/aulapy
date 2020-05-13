import re

def sum(a,b):
    return print(a+b)
def sub(a,b):
    return print(b-a)
def prod(a,b):
    return print(a*b)

case = int(input())
for _ in range(case):
    x,y,z = input()
    x = int(x)
    z = int(z)
    y = ord(y) #converte o caractere para um valor UNICODE referente a sua string
    if x == z:
        prod(x,z)
    elif y >= 65 and y <= 90:
        sub(x,z)
    else:
        sum(x,z)