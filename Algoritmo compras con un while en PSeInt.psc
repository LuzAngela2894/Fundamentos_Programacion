Algoritmo Compras_While
	//Entrada
	Definir nombre_cliente,producto,codigo Como Caracter
	Definir cantidad_general,cantidad_detallada,precio,subtotal,total Como Real
	//Proceso
	Escribir "¿Cuál es el nombre del cliente? "
	leer nombre_cliente
	Escribir "¿Cuántos productos compró? "
	Leer cantidad_general
	Mientras cantidad_general>=1 Hacer
		Escribir "¿Qué producto compró el cliente? "
		leer producto
		Escribir "¿Cuál es el código del producto? "
		leer codigo
		Escribir "¿Cuántos compró? "
		leer cantidad_detallada
		Escribir "¿Cuál es el precio del producto? "
		leer precio
		subtotal=cantidad_detallada*precio
		total=total+subtotal
		cantidad_general=cantidad_general-1
	Fin Mientras
	//Salida
	Escribir nombre_cliente," su valor total a pagar en esta compra es de ",total
FinAlgoritmo
