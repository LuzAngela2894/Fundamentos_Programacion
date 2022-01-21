def check():
    try:
        with open("agenda.txt", "r") as archivo:
            return True
    except FileNotFoundError as no:
        return False
    except IOError as no:
        return False
     
if check() == True:
    print("Este archivo ya existe...")
    exit()
else:
    archivo = open("agenda.txt", "w")
    for i in range(0,11):
        nombre = input("\nNombre y apellido del beneficiario: ")
        cedula = input("Cédula del beneficiario: ")
        celular = input("Celular del beneficiario: ")
        archivo.write(nombre + "\n")
        archivo.write(cedula + "\n")
        archivo.write(celular + "\n")
    archivo.close()
