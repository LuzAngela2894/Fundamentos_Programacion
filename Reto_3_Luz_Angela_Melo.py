t_maxima = 1
t_minima = 1
ma = 0
mi = 0
t_diaria = 0
t_error = 0
cmi = 0
cma = 0
ambas = 0
pma = 0
pmi = 0
t_dias = 0
porcentaje = 0
while t_maxima != 0:
    t_maxima = int(input("Ingresa por favor temperatura máxima: "))
    t_minima = int(input("Ingresa por favor temperatura mínima: "))
    if t_maxima != 0:
        if t_minima >= 5 and 35 >= t_maxima:
            ma = ma + t_maxima
            mi = mi + t_minima
            t_diaria = t_diaria + 1
        else:
            if 5 > t_minima or t_maxima > 35:
                t_error = t_error + 1
            if 5 > t_minima and t_maxima > 35:
                ambas = ambas + 1
            if 5 > t_minima and not t_maxima > 35:
                cmi = cmi + 1
            if t_maxima > 35 and not 5 > t_minima:
                cma = cma + 1
pma = ma / t_diaria
pmi = mi / t_diaria
t_dias = t_diaria + t_error
porcentaje = (t_error / t_dias) * 100
print("N° días que duró la salida de campo:", t_dias)
print("N° días que tuvieron temperaturas con error:", t_error)
print("N° días con temperatura menor a 5°:", cmi)
print("N° días con temperatura mayor a 35°:", cma)
print("N° días con ambos errores:", ambas)
print("Temperatura media máxima:", pma)
print("Temperatura media mínima:", pmi)
print("Porcentaje días de error respecto al total de días:", porcentaje)
