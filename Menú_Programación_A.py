import sys
import math
opcion = 0
print("***************************************************************************************************************")
print("****************************************MENÚ FUNDAMENTOS DE PROGRAMACIÓN***************************************")
print("***************************************************************************************************************")
print("1.Días de la semana")
print("2.Bolita")
print("3.Ecuación cuadrática")
print("4.Subsidio de transporte")
print("5.Ángulo")
print("6.Proceso")
print("7.Par o impar")
print("8.Rango peso")
print("9.Salir")
opcion = int(input("\nSeleccione la opción deseada: "))
if opcion >= 1 and opcion <= 9:

    if opcion == 1:
        numero = int(input("\nIngrese un número por favor: "))
        if numero >= 1 and numero <= 7:
            if numero == 1:
                print("\nEl número ingresado corresponde al día de la semana: LUNES")
            elif numero == 2:
                print("\nEl número ingresado corresponde al día de la semana: MARTES")
            elif numero == 3:
                print("\nEl número ingresado corresponde al día de la semana: MIÉRCOLES")
            elif numero == 4:
                print("\nEl número ingresado corresponde al día de la semana: JUEVES")
            elif numero == 5:
                print("\nEl número ingresado corresponde al día de la semana: VIERNES")
            elif numero == 6:
                print("\nEl número ingresado corresponde al día de la semana: SÁBADO")
            else:
                print("\nEl número ingresado corresponde al día de la semana: DOMINGO")
        else:
            print("\nEl número está fuera del rango 1 a 7, por favor revise.")

    elif opcion == 2:
        nombre = input("\nIngrese el nombre del cliente: ")
        producto = input("\nIngrese el producto: ")
        precio = int(input("\nIngrese el precio: "))
        cantidad = int(input("\nIngrese la cantidad: "))
        subtotal = precio * cantidad
        print("\n¡Tendrás un descuento! Para ello, juega en el sorteo y saca una bola de color.")
        bola = input("\n¿Cuál es el color de la bola? ")
        if bola == "negro" or bola == "rojo" or bola == "verde" or bola == "azul" or bola == "amarillo" or bola == "blanco":
            if bola == "negro":
                dto = int(subtotal * 0.4)
            elif bola == "rojo":
                dto = int(subtotal * 0.3)
            elif bola == "verde":
                dto = int(subtotal * 0.6)
            elif bola == "azul":
                dto = int(subtotal * 0.5)
            elif bola == "amarillo":
                dto = int(subtotal * 0.2)
            elif bola == "blanco":
                dto = 0
            total = int(subtotal - dto)
            print("\nEstimado(a)", nombre, "usted compró:", producto, "el color de la bola fue:", bola,
                  "y el descuento es de:", dto)
            print("\nEl valor total a pagar en esta compra es de:", total)
        else:
            print("\nEl color ingresado no se encuentra en el sorteo. Por favor revisar.")

    elif opcion == 3:
        a = float(input("\nIngrese un número (a) por favor: "))
        b = float(input("\nIngrese un número (b) por favor: "))
        c = float(input("\nIngrese un número (c) por favor: "))
        d = (b ** 2) - (4 * a * c)
        if a == 0:
            print("\nLa ecuacion no es cuadrática")
        elif d == 0:
            x1 = -b / (2 * a)
            x2 = -b / (2 * a)
            print("\nLa solución X1 es", x1)
            print("\nLa solución X2 es", x2)
        elif d > 0:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            print("\nLa solución X1 es", x1)
            print("\nLa solución X2 es", x2)
        elif d < 0:
            print("\nLa solución es un número complejo")
            real = -b / (2 * a)
            imaginario = math.sqrt(abs(d)) / (2 * a)
            print("\nLa solución real es", real)
            print("\nLa solución imaginaria es", imaginario)

    elif opcion == 4:
        nombre = input("\nIngresar el nombre del empleado: ")
        sueldo = int(input("\nIngesar el sueldo del empleado: "))
        smmlv = 908526
        auxilio_transporte = 106454
        salud = int(sueldo * 0.04)
        pension = int(sueldo * 0.04)
        if sueldo <= (smmlv * 2):
            salario = sueldo + auxilio_transporte - salud - pension
            print("\nPara el empleado", nombre, "el total a pagar por concepto de salario es de: $", salario)
        else:
            salario = sueldo - salud - pension
            print("\nPara el empleado", nombre, "el total a pagar por concepto de salario es de: $", salario)

    elif opcion == 5:
        angulo = float(input("\nIngrese el valor del ángulo en grados: "))
        if angulo < 90:
            print("\nEl ángulo se considera AGUDO")
        elif angulo > 90:
            print("\nEl ángulo se considera OBTUSO")
        elif angulo == 90:
            print("\nEl ángulo se considera RECTO")

    elif opcion == 6:
        numero = float(input("\nIngresa un número por favor: "))
        if numero < 0:
            cubo = math.pow(numero, 3)
            print("\nEl número ingresado fue:", numero, "y el resultado del proceso (cubo) es:", cubo)
        elif numero >= 0 and numero <= 100:
            cuadrado = math.pow(numero, 2)
            print("\nEl número ingresado fue:", numero, "y el resultado del proceso (cuadrado) es:", cuadrado)
        elif numero > 100:
            raiz = math.sqrt(numero)
            print("\nEl número ingresado fue:", numero, "y el resultado del proceso (raíz cuadrada) es:", raiz)

    elif opcion == 7:
        numero = float(input("\nIngrese un número por favor: "))
        if numero % 2 == 0:
            print("\n", numero, "Este número es par")
        else:
            print("\n", numero, "Este número es impar")

    elif opcion == 8:
        nombre = input("\nIngrese el nombre del estudiante: ")
        peso = float(input("\nIngrese el peso del estudiante: "))
        if peso < 40:
            print("\nEl estudiante", nombre, "se encuentra en el rango de peso de menos de 40 kg.")
        elif peso >= 40 and peso < 50:
            print("\nEl estudiante", nombre, "se encuentra en el rango de peso entre 40 y 50 kg.")
        elif peso >= 50 and peso < 60:
            print("\nEl estudiante", nombre, "se encuentra en el rango de peso entre más de 50 y menos de 60 kg.")
        elif peso >= 60:
            print("\nEl estudiante", nombre, "se encuentra en el rango de peso igual o más de 60kg.")

    else:
        sys.exit()

else:
    print("Valor equivocado o fuera de rango, por favor revisar.")
