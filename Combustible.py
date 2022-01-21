# 1 milla(mile) = 1609.344 metros(metres)
# 1 galón(gallon) = 3.785411784 litros(litres)

def l100kmtompg(litres):
    gallons = litres / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def mpgtol100km(miles):
    km100 = miles * 1609.344 / 1000 / 100
    litres = 3.785411784
    return litres / km100

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))

#Tu tarea es escribir un par de funciones que conviertan l/100km a mpg(milas por galón), y viceversa.
#Las funciones:
#Se llaman l100kmampg y mpgal100km respectivamente.
#Toman un argumento (el valor correspondiente a sus nombres).
#Complementa el código en el editor.
#Ejecuta tu código y verifica si tu salida es la misma que la nuestra.
#Aquí hay información para ayudarte:
#1 milla = 1609.344 metros.
#1 galón = 3.785411784 litros.
