import timeit

run = timeit.default_timer()
a,b = map(int,input().split())
soma = (a+b) * (b-a+1)/2
print("%i"%soma)    

'''
soma de uma progressao aritimética
é mais rápido que a resolução com for
'''

rn = timeit.default_timer()
print(rn - run)