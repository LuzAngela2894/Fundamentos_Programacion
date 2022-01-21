archivo = open("datos2.txt")
elemento = input("Ingrese elemento a borrar: ")
lineas = archivo.readlines()
indice = 0
encontrado = False
for linea in lineas:
    if linea.strip() == elemento:
        input("Siguiente elemento del archivo: "+lineas[indice+2].strip())
        encontrado = True
    indice = indice + 1
if not encontrado:
    print("No existe ese elemento en el archivo")
