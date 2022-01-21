dto_edad = 0
dto_calificacion = 0
dto_ingreso = 0
dto_total = 0
edad = int(input("Por favor ingresar su edad en años:"))
calificacion = int(input("Por favor ingresar el puntaje:"))
ingreso_familiar = float(input("Por favor ingresar salarios mínimos:"))
if 15 <= edad <= 18:
    dto_edad = 25
elif 19 <= edad <= 21:
    dto_edad = 15
elif 22 <= edad <= 25:
    dto_edad = 10
elif edad > 25:
    dto_edad = 0
if 80 <= calificacion < 86:
    dto_calificacion = 30
elif 86 <= calificacion < 91:
    dto_calificacion = 35
elif 91 <= calificacion < 96:
    dto_calificacion = 40
elif calificacion >= 96:
    dto_calificacion = 45
elif calificacion < 80:
    dto_calificacion = 0
if ingreso_familiar <= 1:
    dto_ingreso = 30
elif 1 < ingreso_familiar <= 2:
    dto_ingreso = 20
elif 2 < ingreso_familiar <= 3:
    dto_ingreso = 10
elif 3 < ingreso_familiar <= 4:
    dto_ingreso = 5
elif ingreso_familiar > 4:
    dto_ingreso = 0
dto_total = dto_edad + dto_calificacion + dto_ingreso
print(dto_edad)
print(dto_calificacion)
print(dto_ingreso)
print(dto_total)
