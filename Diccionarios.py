dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
numerosTelefono = {'jefe' : 5551234567, 'Suzy' : 22657854310}
diccionarioVacio = {}

print(dict)
print(numerosTelefono)
print(diccionarioVacio)

for key in dict.keys():
    print(key, "->", dict[key])

for key in sorted(dict.keys()):
    print(key, "->", dict[key])

for spanish, french in dict.items():
    print(spanish, "->", french)

for french in dict.values():
    print(french)
    
dict['gato'] = 'minou'
dict['cisne'] = 'cygne'
dict.update({"pato" : "canard"})
print(dict)

del dict['perro']
print(dict)
