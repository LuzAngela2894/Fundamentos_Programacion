#Salario

nombre=input("\nIngresar el nombre del empleado: ")
sueldo=int(input("\nIngesar el sueldo del empleado: "))
smmlv=908526
auxilio_transporte=106454
salud=int(sueldo*0.04)
pension=int(sueldo*0.04)

if sueldo<=(smmlv*2):
    salario=sueldo+auxilio_transporte-salud-pension
    print("\nPara el empleado",nombre,"el total a pagar por concepto de salario es de: $",salario)
else:
    salario=sueldo-salud-pension
    print("\nPara el empleado",nombre,"el total a pagar por concepto de salario es de: $",salario)
