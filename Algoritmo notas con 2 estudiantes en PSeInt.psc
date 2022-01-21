Algoritmo notas_2Estudiantes
	// Entrada
	Definir nombreE1,nombreE2,asignaturaE1,asignaturaE2 Como Caracter
	Definir nota1E1,nota2E1,definitivaE1,nota1E2,nota2E2,definitivaE2 Como Real
	// Proceso
	Escribir 'Ingrese el nombre del estudiante 1 '
	Leer nombreE1
	Escribir 'Ingrese el nombre de la asignatura del estudiante 1'
	Leer asignaturaE1
	Escribir 'Ingrese la nota 1 del estudiante 1 '
	Leer nota1E1
	Escribir 'Ingrese la nota 2 del estudiante 1 '
	Leer nota2E1
	definitivaE1 <- (nota1E1+nota2E1)/2
	Escribir 'Ingrese el nombre del estudiante 2 '
	Leer nombreE2	
	Escribir 'Ingrese el nombre de la asignatura del estudiante 2'
	Leer asignaturaE2
	Escribir 'Ingrese la nota 1 del estudiante 2 '
	Leer nota1E2
	Escribir 'Ingrese la nota 2 del estudiante 2 '
	Leer nota2E2
	definitivaE2 <- (nota1E2+nota2E2)/2
	// Salida
	Escribir 'El estudiante ',nombreE1,' obtuvo una definitiva de ',definitivaE1,' en la asignatura ',asignaturaE1
	Escribir 'El estudiante ',nombreE2,' obtuvo una definitiva de ',definitivaE2,' en la asignatura ',asignaturaE2
FinAlgoritmo
