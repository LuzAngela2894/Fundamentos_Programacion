#Matrices o arreglos bidimensionales

#Declarar la matriz

suma = 0
vloar = 0
f = 0
c = 0
d = 2
contador = 0
sumam5 = 0
contam5 = 0
f = int(input("Ingrese el número de filas deseado: "))
c = int(input("Ingrese el número de columnas deseado: "))

#Declarar la matriz

matrizA = [[0 for j in range (c)] for i in range(f)]

#Llenar la matriz

for i in range(0,f):
    for j in range(0,c):
        valor = int(input(f"matrizA[{i}][{j}]= "))
        matrizA[i][j] = valor

#Imprimir una matriz

print("*"*10,"Imprimir matrizA","*"*10)
for i in range(0,f):
    for j in range(0,c):
        print(matrizA[i][j], end = " ")
    print("\n")

#Operaciones con matrices
    
for i in range(0,f):
    for j in range(0,c):
        #sumar pares
        if matrizA[i][j] % 2 == 0:
            suma = suma + matrizA[i][j]
        #cuenta primos
        d = 2
        while matrizA[i][j] % d != 0:
            d = d + 1
            if matrizA[i][j] == d:
                contador = contador + 1
        #promedio de múltiplos de 5
        if matrizA[i][j] % 5 == 0:
            sumam5 = sumam5 + matrizA[i][j]
            contam5 = contam5 + 1
if contam5 > 0:
    promedio = sumam5 / contam5
    print("El promedio de múltiplos de 5 es:",promedio)
else:
    print("No hay múltiplos de 5")

#Imprimir resultados

print("La suma de pares de la matriz es:",suma)
print("La cuenta de primos de la matriz es:",contador)

    
            
        

        

