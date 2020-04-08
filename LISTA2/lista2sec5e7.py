a = int(input(''))
b = int(input(''))
c = int(input(''))

if (a < b +c) or (b < a +c) or (c < a + b):
    if a == b and a == c and b == c:
        print("Triângulo equilátero")
    else:
        if (a == b) and (a == c) and not (b == c) or (a == b) and (a!=c) and (b!=c):
            print("Triângulo isóceles")
        else:
            if (a != b ) and (b != c) and (a != c):
                print("Triângulo escaleno")