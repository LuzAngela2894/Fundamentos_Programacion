#Imprimir si el número ingresado es primo o no

n=int(input("\nIngresa un número por favor: "))
d=2

while n%d!=0:
    d=d+1
if n==d:
    print("\nEl número ingresado es un número primo")
else:
    print("\nEl número ingresado NO es un número primo")
print("\nPrograma Finalizado")

#Imprimir si el número ingresado es primo o no y si desea evaluar más números o no

opcion="S"
d=2

while opcion=="S":
    d=2
    n=int(input("\nIngresa un número por favor: "))
    while n%d!=0:
        d=d+1
    if n==d:
        print("\nEl número ingresado es un número primo")
    else:
        print("\nEl número ingresado NO es un número primo")
    opcion=input("\n¿Desea evaluar más números? S/N ")
print("\nPrograma Finalizado")


