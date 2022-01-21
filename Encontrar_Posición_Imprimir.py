archivo = open("agenda.txt")
buscar = input("Nombre y apellido del beneficiario: ")
linea = 0
posicion = -1
for i in archivo:
    linea = linea + 1
    posicion = i.find(buscar)
    if posicion >= 0:
        print(archivo.readline(linea))
        break