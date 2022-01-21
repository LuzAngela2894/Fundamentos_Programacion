archivo = open("agenda.txt")
nombre = input("Nombre y apellido del beneficiario: ")
cedula = input("Cédula del beneficiario: ")
celular = input("Celular del beneficiario: ")
for i in archivo:
    if i.find(cedula) >= 0:
        print("\nEste beneficiario ya existe...")
        exit()
archivo = open("agenda.txt", "a")
archivo.write("\n" + nombre + "\n")
archivo.write(cedula + "\n")
archivo.write(celular + "\n")
archivo.close()