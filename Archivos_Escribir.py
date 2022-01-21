# "r" -->lectura "w"-->escritura
salida = open("C:/Users/Luz Angela Melo/OneDrive - Universidad Piloto de Colombia/Documents/MinTic/Ciclo 1 Python/Semana 7/salida.txt","w")

linea1 = "Esta es la prueba de escritura en archivos a través de python,\n"
salida.write(linea1)

linea2 = "se verifica el proceso dentro del archivo creado,\n"
salida.write(linea2)

linea3 = "gracias por participar."
salida.write(linea3)

salida.close()

print(salida)