import math

numero = float(input("\nIngresa un número por favor: "))

if numero<0:
    cubo=math.pow(numero,3)
    print("\nEl número ingresado fue:",numero,"y el resultado del proceso (cubo) es:",cubo)
elif numero>=0 and numero<=100:
    cuadrado=math.pow(numero,2)
    print("\nEl número ingresado fue:",numero,"y el resultado del proceso (cuadrado) es:",cuadrado)
elif numero>100:
    raiz=math.sqrt(numero)
    print("\nEl número ingresado fue:",numero,"y el resultado del proceso (raíz cuadrada) es:",raiz)


