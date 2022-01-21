#Variables Globales
def variable_global():
    global a
    print("\nVariable Globlal:",a)
    a = 1
    return

a = 5
variable_global()
print(a)

#Variables Locales
def variable_local():
    a = 2
    print("\nVariable Local:",a)
    return

a = 5
variable_local()
print(a)

#Variable NonLocal
def variablenonlocal():
    def sub_variablenonlocal():
        nonlocal a
        print("\nVariable No Local:",a)
        a = 1
        return

    a = 3
    sub_variablenonlocal()
    print(a)
    return

a = 4
variablenonlocal()
print(a)

#Las funciones son de dos tipos: con retorno y sin retorno. Adicional, las funciones con retorno y sin retorno son de dos tipos:
#con parámetros y sin parámetros.

#Paso por valor
def comer_manzana(manzanas):
    manzanas - 1

manzanas = 5
comer_manzana(manzanas)
print("\nPaso por valor:",manzanas)

def doblar_valor(numero):
    numero = numero * 2

n = 10
doblar_valor (n)
print("\nPaso por valor:",n)

#Paso por referencia
manzanas = 5
def comer_manzana():
    global manzanas
    manzanas = manzanas - 1

comer_manzana()
print("\nPaso por referencia:",manzanas)
