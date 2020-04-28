nums = []
for i in range(1,6):
    nums.append(int(input()))

cont = 0   
for j in nums:
    if j % 2 == 0:
        cont = cont + 1
    else:
        pass

print(cont,"valores pares")