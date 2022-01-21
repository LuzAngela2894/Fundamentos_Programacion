archivo = input("Ingrese el nombre del archivo: ")
nuevo = open(archivo)
contador = 0
for linea in nuevo:
    if linea.startswith("Subject:"):
        contador += 1
print("Hay",contador,"líneas de asunto (subject) en",archivo)