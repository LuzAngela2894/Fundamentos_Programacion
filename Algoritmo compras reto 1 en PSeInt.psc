Algoritmo Compras_Reto1
	// Entrada
	// Las entradas permiten realizar c�lculos y generar las salidas.
	// Es necesario definir las variables donde se almacenar� la informaci�n y especificar que tipo de variables son: Caracter,
	// Entero, Logico y Real.
	Definir nombre_cliente,producto1,codigo1,producto2,codigo2,producto3,codigo3 Como Caracter
	Definir cantidad1,precio1,subtotal1,cantidad2,precio2,subtotal2,cantidad3,precio3,subtotal3,total Como Real
	// Proceso
	// Los procesos son los pasos para generar las salidas.
	// En este caso se solicita el nombre del cliente, producto, c�digo, cantidad y precio, se hace un c�lculo de subtotal ya que
	// son varios productos y para calcular el valor total a pagar de la compra se suman todos los subtotales.
	Escribir 'Nombre del cliente '
	Leer nombre_cliente
	Escribir '�Qu� producto compr� el cliente? '
	Leer producto1
	Escribir '�Cu�l es el c�digo del producto? '
	Leer codigo1
	Escribir '�Cu�ntos compr�? '
	Leer cantidad1
	Escribir '�Cu�l es el precio del producto? '
	Leer precio1
	subtotal1 <- cantidad1*precio1
	Escribir '�Qu� producto compr� el cliente? '
	Leer producto2
	Escribir '�Cu�l es el c�digo del producto? '
	Leer codigo2
	Escribir '�Cu�ntos compr�? '
	Leer cantidad2
	Escribir '�Cu�l es el precio del producto? '
	Leer precio2
	subtotal2 <- cantidad2*precio2
	Escribir '�Qu� producto compr� el cliente? '
	Leer producto3
	Escribir '�Cu�l es el c�digo del producto? '
	Leer codigo3
	Escribir '�Cu�ntos compr�? '
	Leer cantidad3
	Escribir '�Cu�l es el precio del producto? '
	Leer precio3
	subtotal3 <- cantidad3*precio3
	total <- subtotal1+subtotal2+subtotal3
	// Salida
	// Aqu� mostramos los resultados.
	Escribir nombre_cliente,' su valor total a pagar en esta compra es de ',total
FinAlgoritmo
