#Imprimir números primos entre 1 a 20 y break en 11
n=1
while n<=20:
    n=n+1
    d=2
    while n%d!=0:
        d=d+1
    if n==d:
        print(n,end=" ")
        if n==11:
            break
print("\nPrograma Finalizado")
