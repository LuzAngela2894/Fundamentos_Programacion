#añadir elementos a las listas
lista=["a","e","i","o","u"]
lista.append("k")
print(lista)
ter=["b","c","d","h","n"]
lista.extend(ter)
print(lista)

#ordenar listas
prueba=[23,1,5,9,13,76,34,18,4,8,2]
print(prueba)
lista.sort()
print(lista)
prueba.sort()
print(prueba)

#ordenar listas(sort y reverse)
lista=["a","e","i","o","u","b","c","d","h","n"]
prueba=[23,1,5,9,13,76,34,18,4,8,2]
print("\n")
print("*"*8,"Menor a Mayor","*"*8)
lista.sort()
print(lista)
prueba.sort()
print(prueba)
print("\n")
print("*"*8,"Mayor a Menor","*"*8)
lista.reverse()
print(lista)
prueba.reverse()
print(prueba)
print("\n")

#pop(conserva el elemento)
y=prueba.pop()
z=prueba.pop(4)
print(y,z)
print(prueba)

#remove(no conserva el elemento)
s=prueba.remove(5)
print(prueba)

#del(elimina a partir de la ubicación del índice)
del prueba[1:3]
print(prueba)

