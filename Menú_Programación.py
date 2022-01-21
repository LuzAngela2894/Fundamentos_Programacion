import sys

def mayor_que_cero():
    if numero > 0:
        print("\nEl número es mayor que cero")
    else:
        print("\nEl número no es mayor que cero")

def suma_primo():
    suma = 0
    for n in range(2, 21):
        d = 2
        while n % d != 0:
            d = d + 1
        if n == d:
            suma = suma + n
    return suma

def par_o_impar():
    if numero % 2 == 0:
        return True
    else:
        return False

def conteo_primo():
    suma = 0
    contador = 0
    for n in range(2, 31):
        d = 2
        while n % d != 0:
            d = d + 1
        if n == d:
            suma = suma + n
            contador = contador + 1
    return suma, contador

def tablas_multiplicar(tabla, inicio, fin):
    for numero in range(inicio, fin + 1):
        resultado = tabla * numero
        print("\n", tabla, "*", numero, "=", resultado)

def mayuscula(cadena):
    mayuscula = cadena.upper()
    return mayuscula

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

opcion = 1
print("*" * 38)
print("*" * 6, "MENÚ PROGRAMACIÓN", "*" * 6)
print("*" * 38)
while opcion >= 1 and opcion <= 7:
    print("_" * 38)
    print("\n1.Número mayor que cero")
    print("2.Suma de números primos")
    print("3.Número par o impar")
    print("4.Suma y conteo de números primos")
    print("5.Tablas de multiplicar")
    print("6.Convertir a mayúsculas")
    print("7.Serie Fibonacci")
    print("8.Salir")
    opcion = int(input("\nSeleccione la opción deseada: "))
    if opcion == 1:
        numero = int(input("\nIngresar un numero: "))
        mayor_que_cero()
    elif opcion == 2:
        print("\nLa suma de números primos es:", suma_primo())
    elif opcion == 3:
        numero = float(input("\nIngrese un número por favor: "))
        if par_o_impar() == True:
            print("\nEste número es par...")
        else:
            print("\nEste número es impar...")
    elif opcion == 4:
        print("\nLa suma y la cuenta de números primos entre 2 y 30:", conteo_primo())
    elif opcion == 5:
        tabla = int(input("\nIngresa la tabla a realizar: "))
        inicio = int(input("Ingresa desde donde inicia: "))
        fin = int(input("Ingresa hasta donde finaliza: "))
        tablas_multiplicar(tabla, inicio, fin)
    elif opcion == 6:
        cadena = input("\nIngresa nombre en minúsculas: ")
        print("\nMayúsculas:",mayuscula(cadena))
    elif opcion == 7:
        n = int(input("\nIngrese el valor a calcular: "))
        for i in range(0, n + 1):
            if i == 0:
                continue
            else:
                f = fibonacci(i)
                print(f, end=" ")
    else:
        sys.exit(print("\nHa salido del programa"))
else:
    print("Valor equivocado o fuera de rango, por favor revisar.")