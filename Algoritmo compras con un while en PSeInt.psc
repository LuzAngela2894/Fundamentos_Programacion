Algoritmo Compras_While
	//Entrada
	Definir nombre_cliente,producto,codigo Como Caracter
	Definir cantidad_general,cantidad_detallada,precio,subtotal,total Como Real
	//Proceso
	Escribir "�Cu�l es el nombre del cliente? "
	leer nombre_cliente
	Escribir "�Cu�ntos productos compr�? "
	Leer cantidad_general
	Mientras cantidad_general>=1 Hacer
		Escribir "�Qu� producto compr� el cliente? "
		leer producto
		Escribir "�Cu�l es el c�digo del producto? "
		leer codigo
		Escribir "�Cu�ntos compr�? "
		leer cantidad_detallada
		Escribir "�Cu�l es el precio del producto? "
		leer precio
		subtotal=cantidad_detallada*precio
		total=total+subtotal
		cantidad_general=cantidad_general-1
	Fin Mientras
	//Salida
	Escribir nombre_cliente," su valor total a pagar en esta compra es de ",total
FinAlgoritmo
