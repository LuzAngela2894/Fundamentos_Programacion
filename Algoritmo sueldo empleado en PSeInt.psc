Algoritmo Sueldo_Empleado
	// Entrada
	Definir nombre Como Caracter
	Definir valor_hora,horas_trabajadas,total_horas,descuento,sueldo Como Real
	// Proceso
	Escribir 'Nombre del empleado '
	Leer nombre
	Escribir 'Cuál es el valor hora de trabajo '
	Leer valor_hora
	Escribir 'Número de horas trabajadas '
	Leer horas_trabajadas
	total_horas <- valor_hora*horas_trabajadas
	descuento <- total_horas*0.04+total_horas*0.04
	sueldo <- total_horas-descuento
	// Salida
	Escribir 'Para el empleado ',nombre,' su sueldo total a pagar es de ',sueldo
FinAlgoritmo
