datos = []
with open("prueba.txt") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        datos.append(linea.strip("\n"))
print(datos)
buscar = input("Digite el nombre y apellido del beneficiario a buscar: ")
indice = datos.index(buscar)
posicion = "\n".join(datos[indice:indice+3])
print(posicion)