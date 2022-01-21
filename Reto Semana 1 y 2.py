nombre_cliente = input("Ingrese nombre del cliente: ")
n = int(input("Cuántos productos compró en total: "))
suma = 0
total = 0
while n > suma:
    producto = input("Producto: ")
    codigo = input("Código del producto: ")
    cantidad = int(input("Cuántos compró de este producto: "))
    suma = suma + cantidad
    precio = int(input("Precio: "))
    subtotal = cantidad * precio
    total = total + subtotal
print(nombre_cliente, "su valor total a pagar en esta compra es de:", format(total, "0,.2f"))
