# CONVERTIR UN TXT A LISTAS
agenda = []
with open("prueba.txt") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        agenda.append(linea.strip("\n"))
print(agenda)
# FILTRAR LISTAS POR LETRA
letra = input("\nDigite la letra por la que empiezan los beneficiarios: ")
print("*" * 10, "Listado filtrado de Beneficiarios", "*" * 10)
for i in agenda:
    if i.startswith(letra.upper()):
        indice_l = agenda.index(i)
        posicion_l = "\n".join(agenda[indice_l:indice_l+3])
        print(posicion_l)
# BUSCAR ELEMENTOS EN LISTAS
search = input("Digite el nombre y apellido del beneficiario a buscar: ")
indice_s = agenda.index(search)
posicion_s = "\n".join(agenda[indice_s:indice_s+3])
print(posicion_s)
# ELIMINAR ELEMENTOS EN LISTAS Y CONVERTIRLA A TXT
delete = input("Digite la cédula del beneficiario a borrar: ")
indice_d = agenda.index(delete)
del agenda[indice_d]
del agenda[indice_d-1]
del agenda[indice_d-1]
archivo = open("prueba.txt", "w")
posicion_d = "\n".join(agenda[:])
archivo.write(posicion_d)
archivo.close()