Algoritmo notas
	// Entrada
	Definir nombre,asignatura Como Caracter
	Definir nota1,nota2,nota3,definitiva Como Real
	// Proceso
	Escribir 'Ingrese el nombre del estudiante '
	Leer nombre
	Escribir 'Ingrese el nombre de la asignatura '
	Leer asignatura
	Escribir 'Ingrese la nota1 '
	Leer nota1
	Escribir 'Ingrese la nota2 '
	Leer nota2
	Escribir 'Ingrese la nota3 '
	Leer nota3
	definitiva <- nota1*0.3+nota2*0.3+nota3*0.4
	// Salida
	Escribir 'El estudiante ',nombre,' obtuvo una definitiva de ',definitiva,' en la asignatura ',asignatura
FinAlgoritmo
