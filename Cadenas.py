#las cadenas son inmutables

fruta="Banana de Uraba"
print(fruta)

letra=fruta[3]
print(letra)

#recorrer la cadena

indice = 0
while indice < len(fruta):
    letra =fruta[indice]
    print(letra, end = " ")
    indice = indice + 1
print("\n")

#crear cadena desde otra cadena

nueva = "K" + fruta[1:]
print(nueva)

nuevo=fruta.upper()
print(nuevo)

print(nueva.lower())

otra=fruta.find("an")
print(otra)

#operador %(mod) en cadenas

camellos=42
print("Yo he visto %d camellos."%camellos)






