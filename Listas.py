dias=["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
print(dias)

otra=[1,3,"cuatro",5,"ocho"]
print(otra)

nombre="Pedro Martínez"
edad=34
peso="35 Kg"
persona=[nombre,edad,peso]
print(persona)

nueva=dias[1:4]
print(nueva)

#concatenar listas

vocales=["a","e","i"]
vocales += ["o","u"]
print(vocales)

#copiar listas

a = 4
b = 5
c = a
a = a + b
print(a)

lista1=[1,2,3,4,5]
lista2=lista1
print(lista1)
print(lista2)

lista1[2:4]=[9,9]
print(lista1)
print(lista2)

#guardar una lista

lista1=[4,5,6,7,8,9]
print(lista1)
lista2=lista1[:]
lista1[2:4]=[1,2]
print(lista1)
print(lista2)

#recorrer una lista
#forma directa
listo=[0,1,2,3,4,5,6,7,8,9]
for i in listo:
    print(i, end = " ")
print("\n")
#forma indirecta
for i in range(len(listo)):
    print(i, end = " ")
print("\n")
#al revés
for i in range(len(listo)-1,-1,-1):
    print(i, end = " ")
print("\n")
listo=[0,1,2,3,4,5,6,7,8,9]
listo.reverse()
print(listo)

    
    



