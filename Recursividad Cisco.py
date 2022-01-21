def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorialFun(n - 1)

# Implementación recursiva de la función factorial
def factorial(n):
    if n == 1:    # la condición de terminación
        return 1
    else:
        return n * factorial(n - 1)

print("FIBONACCI")
for n in range(1, 10): #Probando
    print(n, "->", fib(n))

print("FACTORIAL")
for n in range(1, 10): #Probando
    print(n, "->", factorialFun(n))

print("FACTORIAL")
for n in range(1, 10): #Probando
    print(n, "->", factorial(n))
