EMPTY = "-"
TORRE = "TORRE"
CABALLO = "CABALLO"
PEON = "PEON"
tablero = []

for i in range(8):
    fila = [EMPTY for i in range(8)]
    tablero.append (fila)

tablero[0][0] = TORRE
tablero[0][7] = TORRE
tablero[7][0] = TORRE
tablero[7][7] = TORRE
tablero[4][2] = CABALLO
tablero[3][4] = PEON

print(tablero)