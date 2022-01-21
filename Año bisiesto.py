def isYearLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


testdata = [1900, 2000, 2016, 1987, 2010]
testresults = [False, True, True, False, True]
for i in range(len(testdata)):
    yr = testdata[i]
    print(yr, "-> ", end="")
    result = isYearLeap(yr)
    if result == testresults[i]:
        print("OK")
    else:
        print("Error")

# Tu tarea es escribir y probar una función que
# toma un argumento (un año) y devuelve True si el año es un año bisiesto, o False sí no lo es.
# Parte del esqueleto de la función ya está en el editor.
# Nota: también hemos preparado un breve código de prueba, que puedes utilizar para probar tu función.
# El código utiliza dos listas: una con los datos de prueba y la otra con los resultados esperados.
# El código te dirá si alguno de tus resultados no es válido.
