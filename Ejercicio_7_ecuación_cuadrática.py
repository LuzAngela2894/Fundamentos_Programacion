import math

a=float(input("\nIngrese un número (a) por favor: "))
b=float(input("\nIngrese un número (b) por favor: "))
c=float(input("\nIngrese un número (c) por favor: "))
d=(b**2)-(4*a*c)

if a==0:
    print("\nLa ecuacion no es cuadrática") 
elif d==0:
    x1= -b / (2*a)
    x2= -b / (2*a)
    print("\nLa solución X1 es",x1)
    print("\nLa solución X2 es",x2)
elif d>0:
    x1= (-b+math.sqrt(d)) / (2*a)
    x2= (-b-math.sqrt(d)) / (2*a)
    print("\nLa solución X1 es",x1)
    print("\nLa solución X2 es",x2)
elif d<0:
    print("\nLa solución es un número complejo")
    real= -b / (2*a)
    imaginario= math.sqrt(abs(d)) / (2*a)
    print("\nLa solución real es",real)
    print("\nLa solución imaginaria es",imaginario)


