def eliminar():
    archivo = open("agenda.txt", "r+")
    cedula = input("Digite la cédula del beneficiario a borrar: ")
    lineas = archivo.readlines()
    salida = lineas
    i = 0
    for linea in lineas:
        if linea.strip() == cedula:
            nombre = lineas[i - 1]
            telefono = lineas[i + 1]
            salida.remove(nombre)
            salida.remove(telefono)
            salida.remove(cedula + "\n")
            archivo.truncate(0)
            archivo.seek(0)
            for line in salida:
                archivo.write(line)
                archivo.flush()
            break
        i = i + 1
    archivo.close()


eliminar()
print("El beneficiario ha sido eliminado")
archivo = open("agenda.txt")
print(archivo.read())
