while True:
    x, y = map(int,input().split())

    if x == 0 and y == 0:
        break
    
    else:
        x = str(x)
        y = str(y)
        b = y.replace(x, '')
        if b == '':
            print(0)
        else:
            y = int(b)
            print(y)