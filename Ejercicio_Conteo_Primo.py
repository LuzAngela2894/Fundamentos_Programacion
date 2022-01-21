def conteo_primo():
    suma = 0
    contador = 0
    for n in range(2,31):
        d = 2
        while n%d != 0:
            d = d + 1
        if n == d:
            suma = suma + n
            contador = contador + 1
    return suma, contador

print("\nLa suma y la cuenta de números primos entre 2 y 30:",conteo_primo())
