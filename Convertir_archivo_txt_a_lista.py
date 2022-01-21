datos = [ ]
with open("agenda.txt") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        datos.append(linea.strip("\n"))
print(datos)
