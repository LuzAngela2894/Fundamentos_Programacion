miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
nuevaLista = []
for numero in miLista: # Explorar todos los números de la lista original.
    if numero not in nuevaLista: # Si el número no aparece en la nueva lista ...
        nuevaLista.append(numero) # ... adjúntalo aquí.
miLista = nuevaLista[:] # Hacer una copia de nuevalista.
print("La lista solo con elementos únicos: ")
print(miLista)
