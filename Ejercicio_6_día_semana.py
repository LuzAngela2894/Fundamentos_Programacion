#Número correspondiente al día de la semana

numero=int(input("\nIngrese un número por favor: "))

if numero>=1 and numero<=7:
    
    if numero==1:
        print("\nEl número ingresado corresponde al día de la semana: LUNES")
    elif numero==2:
        print("\nEl número ingresado corresponde al día de la semana: MARTES")
    elif numero==3:
        print("\nEl número ingresado corresponde al día de la semana: MIÉRCOLES")
    elif numero==4:
        print("\nEl número ingresado corresponde al día de la semana: JUEVES")
    elif numero==5:
        print("\nEl número ingresado corresponde al día de la semana: VIERNES")
    elif numero==6:
        print("\nEl número ingresado corresponde al día de la semana: SÁBADO")
    else:
        print("\nEl número ingresado corresponde al día de la semana: DOMINGO")
        
else:
    print("\nEl número está fuera del rango 1 a 7, por favor revise.")
