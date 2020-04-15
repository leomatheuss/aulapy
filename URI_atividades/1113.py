while True:
    a, b = input().split(" ")
    a = int(a)
    b = int(b)

    if b < a:
        print("Decrescente")
    elif b > a:
        print("Crescente")
    
    if a == b or b == a:
        break