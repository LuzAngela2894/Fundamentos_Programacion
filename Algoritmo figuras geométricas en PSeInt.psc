Algoritmo Figuras_Geométricas
	// Entrada
	Definir base,altura,lado,radio,a_triangulo,a_rectangulo,a_circulo Como Real
	// Proceso
	Escribir 'Ingrese la base: '
	Leer base
	Escribir 'Ingrese la altura: '
	Leer altura
	Escribir 'Ingrese el lado: '
	Leer lado
	Escribir 'Ingrese el radio: '
	Leer radio
	a_triangulo <- (base*altura)/2
	a_rectangulo <- base*altura
	a_circulo <- pi*(radio^2)
	// Escribir
	Escribir 'El área del triángulo es: ',a_triangulo
	Escribir 'El área del rectángulo es: ',a_rectangulo
	Escribir 'El áreal del círculo es: ',a_circulo
FinAlgoritmo
