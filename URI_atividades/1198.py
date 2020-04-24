try:
  while True:
    x,y = map(int,input().split())
    if y>x:
      print(y-x)
    elif x>y:
      print(x-y)
    elif x==y:
      print(0)
except:
  pass