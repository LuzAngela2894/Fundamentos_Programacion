def sueldo_b(n_hora, v_hora):
    if n_hora > 40:
        v_extra = v_hora * 1.5 * (n_hora - 40)
        v_normal = 40 * v_hora
    else:
        v_extra = 0
        v_normal = n_hora * v_hora
    sueldo_bruto = v_extra + v_normal
    return sueldo_bruto, v_normal, v_extra


def dto(sueldo_bruto):
    parafiscales = (sueldo_bruto * 9) / 100
    salud = (sueldo_bruto * 4) / 100
    pension = (sueldo_bruto * 4) / 100
    descuentos = parafiscales + salud + pension
    return parafiscales, salud, pension, descuentos


def sueldo_n(sueldo_bruto, descuentos):
    sueldo_neto = sueldo_bruto - descuentos
    return sueldo_neto


def provision(sueldo_bruto):
    prima_servicios = (sueldo_bruto * 8.33) / 100
    cesantias = (sueldo_bruto * 8.33) / 100
    intereses_cesantias = (sueldo_bruto * 1) / 100
    vacaciones = (sueldo_bruto * 4.17) / 100
    return prima_servicios, cesantias, intereses_cesantias, vacaciones


n_hora = int(input("Número horas: "))
v_hora = int(input("Valor horas: "))
sueldo_bruto, v_normal, v_extra = sueldo_b(n_hora, v_hora)
parafiscales, salud, pension, descuentos = dto(sueldo_bruto)
sueldo_neto = sueldo_n(sueldo_bruto, parafiscales + salud + pension)
prima_servicios, cesantias, intereses_cesantias, vacaciones = provision(sueldo_bruto)
print("-" * 28)
print("Valor hora normal:", format(v_normal, "0,.2f"))
print("-" * 28)
print("Valor hora extra:", format(v_extra, "0,.2f"))
print("-" * 28)
print("Sueldo Bruto:", format(sueldo_bruto, "0,.2f"))
print("-" * 28)
print("*" * 8, "DESCUENTOS", "*" * 8)
print("Parafiscales:", format(parafiscales, "0,.2f"))
print("Salud:", format(salud, "0,.2f"))
print("Pensión:", format(pension, "0,.2f"))
print("Descuentos:", format(descuentos, "0,.2f"))
print("-" * 28)
print("Sueldo Neto:", format(sueldo_neto, "0,.2f"))
print("-" * 28)
print("*" * 8, "PROVISIONES", "*" * 8)
print("Prima de servicios:", format(prima_servicios, "0,.2f"))
print("Cesantías:", format(cesantias, "0,.2f"))
print("Intereses de cesantías:", format(intereses_cesantias, "0,.2f"))
print("Vacaciones:", format(vacaciones, "0,.2f"))
print("-" * 28)
