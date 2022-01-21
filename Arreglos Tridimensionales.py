habitaciones = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

habitaciones[1][9][13] = True

habitaciones[0][4][1] = False

vacante = 0

for numeroHabitacion in range(20):
    if not habitaciones[2][14][numeroHabitacion]:
        vacante += 1
print(vacante)
