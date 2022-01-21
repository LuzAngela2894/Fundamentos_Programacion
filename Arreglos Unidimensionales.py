#arreglos en python

#declarar arreglo

arregloA=[ ]

#llenar el arreglo

valor=0
n=int(input("Tamaño del arreglo: "))
for i in range(0,n):
    valor=int(input(f"arregloA[{i}]= "))
    arregloA.append(valor)

#imprimir un arreglo sin recorrido 
print(arregloA) 

#imprimir un arreglo con recorrido
for i in range(0,n): 
    print(arregloA[i],end = " ")

#imprimir posiciones de un arreglo
print("\n",arregloA[3])
print(arregloA[:-2])
print(arregloA[2:])

#operaciones con arreglos
suma=0
contador=0
for i in range(0,n):
    suma=suma+arregloA[i]
    contador=contador+1
promedio=suma/contador
print("\nEl promedio es: ",promedio)

#buscar dentro de un arreglo
encontrado=0
buscar=0
contador=0
buscar=int(input("\n¿Qué dato desea buscar? "))
for i in range(0,n):
    if buscar == arregloA[i]:
        contador=contador+1
        encontrado=i
print("Dato",buscar,"fue encontrado en la posición",encontrado,"cantidad de veces",contador)

#ordenamiento de un arrerglo
auxiliar=0
for i in range(0,n-1): #recorrer el arreglo con i
    for j in range(i+1,n): #recorrer el arreglo con j
        if arregloA[i]>=arregloA[j]: #comparar los arreglos
            auxiliar = arregloA[i]
            arregloA[i]=arregloA[j] #intercambia valores
            arregloA[j]=auxiliar #retorna el valor del auxiliar

#imprimir el arreglo ordenado
print("*"*8,"Arreglo Ordenado","*"*8)
print(arregloA)
for i in range(0,n): 
    print(arregloA[i],end = " ")
