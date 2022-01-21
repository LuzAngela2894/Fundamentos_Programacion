import sys


def search(buscar):
    agenda = []
    with open("agenda.txt") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            agenda.append(linea.strip("\n"))
    indice_b = agenda.index(buscar)
    posicion_b = "\n".join(agenda[indice_b:indice_b + 3])
    return posicion_b


def add():
    archivo = open("agenda.txt", "a")
    archivo.write(nombre + "\n")
    archivo.write(cedula + "\n")
    archivo.write(celular + "\n")
    archivo.close()


def delete(borrar):
    agenda = []
    with open("agenda.txt") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            agenda.append(linea.strip("\n"))
    indice_d = agenda.index(borrar)
    del agenda[indice_d]
    del agenda[indice_d - 1]
    del agenda[indice_d - 1]
    archivo = open("agenda.txt", "w")
    posicion_d = "\n".join(agenda[:])
    archivo.write(posicion_d)
    archivo.close()


opcion = 1
while opcion >= 1 and opcion <= 6:
    print("\nMenu Principal")
    print("1. Ver listado \n2. Ver listado filtrado \n3. Agregar beneficiario \n4. Buscar beneficiario")
    print("5. Borrar beneficiario \n6. Salir \n")
    opcion = int(input())
    if opcion == 1:
        archivo = open("agenda.txt")
        print("Listado de beneficiarios\n")
        print(archivo.read())
    elif opcion == 2:
        agenda = []
        with open("agenda.txt") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                agenda.append(linea.strip("\n"))
        letra = input("Digite la letra por la que empiezan los beneficiarios:\n")
        print("Listado filtrado de beneficiarios:\n")
        for i in agenda:
            if i.startswith(letra.upper()):
                indice_l = agenda.index(i)
                posicion_l = "\n".join(agenda[indice_l:indice_l + 3])
                print(posicion_l)
                break
    elif opcion == 3:
        print("Digite la información del beneficiario a agregar:")
        nombre = input()
        cedula = input()
        celular = input()
        add()
        print("El beneficiario ha sido agregado")
    elif opcion == 4:
        archivo = open("agenda.txt")
        buscar = input("Digite el nombre y apellido del beneficiario a buscar:\n")
        posicion = -1
        for i in archivo:
            posicion = i.find(buscar)
            if posicion >= 0:
                print(search(buscar))
                break
        else:
            print("No se encuentra el beneficiario en la agenda")
    elif opcion == 5:
        borrar = input("Digite la cedula del beneficiario a borrar:\n")
        delete(borrar)
        print("El usuario ha sido eliminado del listado")
    else:
        sys.exit(print("Hasta pronto"))
