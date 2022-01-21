def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
#Programa Principal
n=int(input("Ingrese el valor a calcular: "))
for i in range(0,n+1):
    if i == 0:
        continue
    else:
        f = fibonacci(i)#Paso por referencia
        print(f, end=" ")

#Otra forma
def fibonacci(n):
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    elif n == 0:
        return 0
    elif n == 1:
        return 1
#Programa Principal
n=int(input("\nIngrese el valor a calcular: "))
for i in range(0,n+1):
    f = fibonacci(i)
    print(f,end=" ")

def hanoi(n):
    if n > 1:
        contador = (2 * hanoi(n - 1) + 1)
    else:
        contador = 1
    return contador
n = int(input("\nIntroduzca el número total de discos de la Torre de Hanoi: "))
print("Para",n,"discos, se generan",hanoi(n),"jugadas")

    
    

