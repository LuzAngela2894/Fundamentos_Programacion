def suma_primo():
    suma = 0
    for n in range(2,21):
        d = 2
        while n%d != 0:
            d = d + 1
        if n == d:
            suma = suma + n
    return suma

print("\nLa suma de números primos es:",suma_primo())
    
  

    
    
