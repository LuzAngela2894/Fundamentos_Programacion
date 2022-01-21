archivo = open(
    "C:/Users/Luz Angela Melo/OneDrive - Universidad Piloto de Colombia/Documents/MinTic/Ciclo 1 Python/Semana 7/datos1.txt")
# Contador de líneas
contador = 0
for i in archivo:
    contador = contador + 1
print("El archivo tiene", contador, "líneas")

archivo = open(
    "C:/Users/Luz Angela Melo/OneDrive - Universidad Piloto de Colombia/Documents/MinTic/Ciclo 1 Python/Semana 7/datos1.txt")
# Contador de caracteres
print("El archivo tiene un total de", len(archivo.read()), "caracteres")

archivo = open(
    "C:/Users/Luz Angela Melo/OneDrive - Universidad Piloto de Colombia/Documents/MinTic/Ciclo 1 Python/Semana 7/datos1.txt")
# Cuantas veces se encuentra una palabra
cuenta = 0
for j in archivo:
    if j.find("Colombia") != -1:
        cuenta = cuenta + 1
print("Número de veces que se encuentra esa palabra", cuenta)