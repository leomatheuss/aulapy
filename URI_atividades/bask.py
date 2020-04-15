def raizes (a,b,c):
    delta = (b**2 -4*a*c)
    delta = round(delta, 4)
    if a == 0 or delta < 0:
        print("Impossivel calcular")
    else:
        R1 = (-b + delta**(1/2))/ (2*a)
        R2 = (-b - delta**(1/2))/(2*a)
    
    
        print("R1 = %.5f"% R1)

        print("R2 = %.5f"% R2)

a,b,c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)
raizes(a,b,c)