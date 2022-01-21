#Si cantidad es mayor que 50 aplicar descuento del 30%

producto=input("\nIngrese el producto: ")
precio=int(input("\nIngrese el precio: "))
cantidad=int(input("\nIngrese la cantidad: "))
subtotal=precio*cantidad
descuento=0

if cantidad>50:
   descuento=int(subtotal*0.3)

total=subtotal-descuento
print("\nEl valor total a pagar por el producto",producto,"es de: $",total,"\ny el descuento fue por: $",descuento)

#Si cantidad es mayor que 50 aplicar descuento del 30% en caso contrario no hacer descuento

producto=input("\nIngrese el producto: ")
precio=int(input("\nIngrese el precio: "))
cantidad=int(input("\nIngrese la cantidad: "))
subtotal=precio*cantidad
descuento=int(subtotal*0.3)

if cantidad>50:
    total=subtotal-descuento
    print("\nEl valor total a pagar por el producto",producto,"es de: $",total,"\ny el descuento fue por: $",descuento)
else:
    total=subtotal
    print("\nEl valor total a pagar por el producto",producto,"es de: $",total,"\nNo aplica el descuento")

