def isPrime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True


for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()

# Tu tarea es escribir una función que verifique si un número es primo o no.
# La función:
# Se llama isPrime.
# Toma un argumento (el valor a verificar).
# Devuelve True si el argumento es un número primo, y False de lo contrario.
# Sugerencia: intenta dividir el argumento por todos los valores posteriores (comenzando desde 2) y verifica el resto:
# si es cero, tu número no puede ser un número primo; analiza cuidadosamente cuándo deberías detener el proceso.
# Si necesitas conocer la raíz cuadrada de cualquier valor, puedes utilizar el operador **.
# Recuerda: la raíz cuadrada de x es la misma que x0.5
