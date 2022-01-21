f = int(input("\nNúmero de filas: "))
c = int(input("Número de columnas: "))

ajedrez = [[0 for j in range(c)] for i in range(f)]

for i in range(0, f):
    peon = 1
    for j in range(0, c):
        ajedrez[1][j] = peon
        ajedrez[6][j] = peon * -1
    peon = 1
    for j in range(0, 5):
        ajedrez[0][j] = peon + 1
        ajedrez[7][j] = (peon + 1) * -1
        peon = peon + 1
    peon = 1
    for j in range(7, 4, -1):
        ajedrez[0][j] = peon + 1
        ajedrez[7][j] = (peon + 1) * -1
        peon = peon + 1

print("\n", "*" * 10, "Imprimir Ajedrez", "*" * 10)
for i in range(0, f):
    for j in range(0, c):
        print(ajedrez[i][j], end=" ")
    print("\n")
