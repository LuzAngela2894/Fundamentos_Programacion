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
    archivo = open("agenda.txt", "a+")
    for i in archivo:
        if i.find(cedula) >= 0:
            print("Este beneficiario ya existe...")
            break
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
while 1 <= opcion <= 6:
    print("*" * 25, "MENÚ", "*" * 25)
    print("1. Ver listado \n2. Ver listado filtrado \n3. Agregar beneficiario \n4. Buscar beneficiario")
    print("5. Borrar beneficiario \n6. Salir")
    print("-" * 56)
    opcion = int(input("¿Qué proceso del menú necesita realizar? "))
    if opcion == 1:
        archivo = open("agenda.txt")
        print("*" * 10, "Listado de Beneficiarios", "*" * 10)
        print(archivo.read())
    elif opcion == 2:
        agenda = []
        with open("agenda.txt") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                agenda.append(linea.strip("\n"))
        letra = input("Digite la letra por la que empiezan los beneficiarios: ")
        print("*" * 10, "Listado filtrado de Beneficiarios", "*" * 10)
        for i in agenda:
            if i.startswith(letra.upper()):
                indice_l = agenda.index(i)
                posicion_l = "\n".join(agenda[indice_l:indice_l + 3])
                print(posicion_l)
                break
        else:
            print("No se encuentra la letra a filtrar")
    elif opcion == 3:
        print("Digite la información del benefeciario a agregar:")
        nombre = input("Nombre y apellido: ")
        cedula = input("Cédula: ")
        celular = input("Celular: ")
        add()
        print("El beneficiario ha sido agregado al listado")
    elif opcion == 4:
        archivo = open("agenda.txt")
        buscar = input("Digite el nombre y apellido del beneficiario a buscar: ")
        posicion = -1
        for i in archivo:
            posicion = i.find(buscar)
            if posicion >= 0:
                print(search(buscar))
                break
        else:
            print("No se encuentra el beneficiario en la agenda")
    elif opcion == 5:
        borrar = input("Digite la cédula del beneficiario a borrar: ")
        delete(borrar)
        print("El usuario ha sido eliminado del listado")
    else:
        sys.exit(print("Hasta pronto..."))
else:
    print("Opción no válida...")
