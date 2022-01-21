def isYearLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def daysInMonth(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = days[month - 1]
    if month == 2 and isYearLeap(year):
        res = 29
    return res


def dayOfYear(year, month, day):
    days = 0
    for m in range(1, month):
        md = daysInMonth(year, m)
        if md == None:
            return None
        days += md
    md = daysInMonth(year, month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None


print(dayOfYear(2000, 12, 31))

# Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes)
# y devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.
# Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos de prueba al código.
# Esta prueba es solo el comienzo.
