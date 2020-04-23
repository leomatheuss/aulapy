def media (a, b):
    media = (a*0.35 + b*0.75) / 1.1
    return print("MEDIA = {:.5f}".format(media))

x = float(input())
y = float(input())
media(x,y)
