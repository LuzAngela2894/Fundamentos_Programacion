archivo = input("Ingrese el nombre del archivo: ")
try:
    nuevo = open(archivo)
except:
    print("No se puede abrir su archivo")
    exit()
contador = 0
for linea in nuevo:
    if linea.startswith("Subject:"):
        contador+=1
print("Hay",contador,"líneas de asunto (subject) en",archivo)