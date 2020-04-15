S = 0
y = 0

for i in range(1, 40, 2):
    S = S + i/(2**y)
    y = y + 1
print('%.2f' %S)