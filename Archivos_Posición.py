archivo = open("C:/Users/Luz Angela Melo/OneDrive - Universidad Piloto de Colombia/Documents/MinTic/Ciclo 1 Python/Semana 7/inbox.txt")
for linea in archivo:
    if linea.startswith("From:"):
        print(linea)