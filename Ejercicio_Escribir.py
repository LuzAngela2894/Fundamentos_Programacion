salida = open(
    "C:/Users/Luz Angela Melo/OneDrive - Universidad Piloto de Colombia/Documents/MinTic/Ciclo 1 Python/Semana 7/datos2.txt",
    "w")

salida.write("Angela\n")
salida.write("26\n")
salida.write("Colombia\n")
salida.write("Felipe\n")
salida.write("28\n")
salida.write("Colombia\n")
salida.write("Santiago\n")
salida.write("25\n")
salida.write("Mexico\n")
salida.write("Lucía\n")
salida.write("23\n")
salida.write("Mexico\n")

salida.close()

archivo = open(
    "C:/Users/Luz Angela Melo/OneDrive - Universidad Piloto de Colombia/Documents/MinTic/Ciclo 1 Python/Semana 7/datos2.txt",
    "r")
# Contador de líneas
contador = 0
for i in archivo:
    contador = contador + 1
print("Número de líneas que el archivo tiene", contador)

archivo = open(
    "C:/Users/Luz Angela Melo/OneDrive - Universidad Piloto de Colombia/Documents/MinTic/Ciclo 1 Python/Semana 7/datos2.txt")
# Contador de caracteres
print("El archivo tiene un total de", len(archivo.read()), "caracteres")

archivo = open(
    "C:/Users/Luz Angela Melo/OneDrive - Universidad Piloto de Colombia/Documents/MinTic/Ciclo 1 Python/Semana 7/datos2.txt")
# Cuantas veces se encuentra una palabra
cuenta = 0
for j in archivo:
    if j.find("Colombia") != -1:
        cuenta = cuenta + 1
print("Número de veces que se encuentra esa palabra", cuenta)