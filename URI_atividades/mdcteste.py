def mdc(x,y):
   
    mdc1 = x
    while x % mdc1 != 0 or y % mdc1 != 0:
        mdc1 = mdc1 - 1
    return print(mdc1)



f1 = int(input())
f2 = int(input())

mdc(f1, f2)