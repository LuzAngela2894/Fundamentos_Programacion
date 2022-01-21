print("\nRecuerde que la escala de notas va de 0 a 5, siendo 5 la nota más alta y 0 la nota más baja.\n")
nota=1
suma=0
contador=0
aprobo=0
reprobo=0
minimo=5
maximo=0
while nota>=0 and nota<=5:
    nota=float(input("Ingrese la nota definitiva de física del estudiante: "))
    if nota>=0 and nota<=5:
        if nota>=maximo:
            maximo=nota
        elif nota<=minimo:
            minimo=nota
        if nota>=3:
            aprobo=aprobo+1
        else:
            reprobo=reprobo+1
        suma=suma+nota
        contador=contador+1
    else:
        print("\nFin del ingreso de notas...")
promedio=suma/contador
print("\nCantidad de estudiantes que aprobaron:",aprobo)
print("\nCantidad de estudiantes que NO aprobaron:",reprobo)
print("\nLa máxima nota fue de {} y la mínima nota fue de {}".format(maximo,minimo))
print("\nEl promedio de notas de los estudiantes es igual a:",format(promedio,"0.2f"))
print("\nPrograma finalizado...")



        




    

