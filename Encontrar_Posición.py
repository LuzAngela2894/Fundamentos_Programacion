archivo = open("agenda.txt")
buscar = input("Nombre y apellido del beneficiario: ")
posicion = -1
linea = 0
for i in archivo:
    linea = linea + 1
    posicion = i.find(buscar)
    if posicion >= 0:
        print("El beneficiario se encuentra en la linea %i" % linea)
        break