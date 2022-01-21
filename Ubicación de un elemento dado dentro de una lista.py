miLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Encontrar = 5
Encontrado = False

for i in range(len(miLista)):
    Encontrado = miLista[i] == Encontrar
    if Encontrado:
        break

if Encontrado:
    print("Elemento encontrado en el índice", i)
else:
    print("\nausente")

#Nota:
#El valor buscado se almacena en la variable Encontrar.
#El estado actual de la búsqueda se almacena en la variable Encontrado (True/False).
#Cuando Encontrado se convierte en True, se sale del bucle for.

sorteados = [5, 11, 9, 42, 3, 49]
seleccionados = [3, 7, 11, 42, 34, 49]
aciertos = 0

for numeros in seleccionados:
    if numeros in sorteados:
        aciertos += 1

print("\n",aciertos)

#Nota:
#La lista sorteados almacena todos los números ganadores.
#La lista de seleccionados almacena con números con que se juega.
#La variable aciertos cuenta tus aciertos.
