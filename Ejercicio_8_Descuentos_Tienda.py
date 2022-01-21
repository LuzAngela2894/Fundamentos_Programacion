nombre=input("\nIngrese el nombre del cliente: ")
producto=input("\nIngrese el producto: ")
precio=int(input("\nIngrese el precio: "))
cantidad=int(input("\nIngrese la cantidad: "))
subtotal=precio*cantidad

print("\n¡Tendrás un descuento! Para ello, juega en el sorteo y saca una bola de color.")
bola=input("\n¿Cuál es el color de la bola? ")

if bola=="negro" or bola=="rojo" or bola=="verde" or bola=="azul" or bola=="amarillo" or bola=="blanco":

    if bola=="negro":
        dto=int(subtotal*0.4)
    elif bola=="rojo":
        dto=int(subtotal*0.3)
    elif bola=="verde":
        dto=int(subtotal*0.6)
    elif bola=="azul":
        dto=int(subtotal*0.5)
    elif bola=="amarillo":
        dto=int(subtotal*0.2)
    elif bola=="blanco":
        dto=0
    total=int(subtotal-dto)
    print("\nEstimado(a)",nombre,"usted compró:",producto,"el color de la bola fue:",bola,"y el descuento es de:",dto)
    print("\nEl valor total a pagar en esta compra es de:",total)

else:
    print("\nEl color ingresado no se encuentra en el sorteo. Por favor revisar.")

