def tablas_multiplicar(tabla,inicio,fin):
    for numero in range(inicio,fin+1):
        resultado = tabla * numero
        print(tabla,"*",numero,"=",resultado)

tabla = int(input("\nIngresa la tabla a realizar: "))
inicio = int(input("\nIngresa desde donde inicia: "))
fin = int(input("\nIngresa hasta donde finaliza: "))
tablas_multiplicar(tabla,inicio,fin)