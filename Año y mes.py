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


testyears = [1900, 2000, 2016, 1987]
testmonths = [2, 2, 1, 11]
testresults = [28, 29, 31, 30]
for i in range(len(testyears)):
    yr = testyears[i]
    mo = testmonths[i]
    print(yr, mo, "-> ", end="")
    result = daysInMonth(yr, mo)
    if result == testresults[i]:
        print("OK")
    else:
        print("Error")

# Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el número de días del
# mes/año dado (mientras que solo febrero es sensible al valor year, tu función debería ser universal).
# La parte inicial de la función está lista. Ahora, haz que la función devuelva None si los argumentos no tienen sentido.
# Por supuesto, puedes (y debes) utilizar la función previamente escrita y probada (LAB 4.1.3.6).
# Puede ser muy útil. Te recomendamos que utilices una lista con los meses. Puedes crearla dentro de la función;
# este truco acortará significativamente el código.
