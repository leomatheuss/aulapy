import timeit

start = timeit.default_timer()
a = [8,5,12,55,3,7,82,44,35,25,41,29,17]
b = a.sort()
print(a)
print(b)
stop = timeit.default_timer()
print("Time:", stop - start)