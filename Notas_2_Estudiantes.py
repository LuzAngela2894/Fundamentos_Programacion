#Algoritmo para encontrar la definitiva de dos estudiantes
#Entradas
nombreE1=" "
asignaturaE1=" "
nota1E1=0
nota2E1=0
nota3E1=0
definitivaE1=0
nombreE2=" "
asignaturaE2=" "
nota1E2=0
nota2E2=0
nota3E2=0
definitivaE2=0
#Proceso
nombreE1=input("\nIngrese el nombre del estudiante 1 ")
asignaturaE1=input("\nIngrese la asignatura del estudiante 1 ")
nota1E1=float(input("\nIngrese la nota 1 del estudiante 1 "))
nota2E1=float(input("\nIngrese la nota 2 del estudiante 1 "))
nota3E1=float(input("\nIngrese la nota 3 del estudiante 1 "))
definitivaE1=nota1E1*0.3+nota2E1*0.3+nota3E1*0.4
nombreE2=input("\nIngrese el nombre del estudiante 2 ")
asignaturaE2=input("\nIngrese la asignatura del estudiante 2 ")
nota1E2=float(input("\nIngrese la nota 1 del estudiante 2 "))
nota2E2=float(input("\nIngrese la nota 2 del estudiante 2 "))
nota3E2=float(input("\nIngrese la nota 3 del estudiante 2 "))
definitivaE2=nota1E2*0.3+nota2E2*0.3+nota3E2*0.4
#Salidas
print("\nEl estudiante",nombreE1,"obtuvo una definitiva de",definitivaE1,"en la asignatura",asignaturaE1)
print("\nEl estudiante",nombreE2,"obtuvo una definitiva de",definitivaE2,"en la asignatura",asignaturaE2)
