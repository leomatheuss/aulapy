food = [300, 1500, 600, 1000, 150]
x = []
for i in range(1, 6):
    x.append(int(input()))
zipped = zip(food, x)
mult = [x*food for x,food in zipped]
#map()
print(sum(mult) + 225)