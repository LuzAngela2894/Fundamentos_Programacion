def par_o_impar():
    if numero%2==0:
        return True
    else:
        return False

numero = float(input("\nIngrese un número por favor: "))
if par_o_impar() == True:
    print("\nEste número es par...")
else:
    print("\nEste número es impar...")

