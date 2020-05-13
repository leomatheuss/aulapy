import math

try:
    while True:
        d, vf, vg = map(int,input().split())

        dist = math.sqrt(144 + d**2)
        tf = 12/vf
        tg = dist/vg

        if tg <= tf:
            print('S')
        else:
            print('N')
        
except EOFError:
    pass