f = int(input("Número de filas: "))
c = int(input("Número de columnas: "))

matrizA = [[0 for j in range(c)] for i in range(f)]

for i in range(0, f):
    for j in range(0, c):
        matrizA[0][0] = 2
        matrizA[0][1] = 3
        matrizA[0][2] = 4
        matrizA[0][3] = 5
        matrizA[0][4] = 6
        matrizA[0][5] = 4
        matrizA[0][6] = 3
        matrizA[0][7] = 2
        matrizA[1][0] = 1
        matrizA[1][1] = 1
        matrizA[1][2] = 1
        matrizA[1][3] = 1
        matrizA[1][4] = 1
        matrizA[1][5] = 1
        matrizA[1][6] = 1
        matrizA[1][7] = 1
        matrizA[6][0] = -1
        matrizA[6][1] = -1
        matrizA[6][2] = -1
        matrizA[6][3] = -1
        matrizA[6][4] = -1
        matrizA[6][5] = -1
        matrizA[6][6] = -1
        matrizA[6][7] = -1
        matrizA[7][0] = -2
        matrizA[7][1] = -3
        matrizA[7][2] = -4
        matrizA[7][3] = -5
        matrizA[7][4] = -6
        matrizA[7][5] = -4
        matrizA[7][6] = -3
        matrizA[7][7] = -2

print("\n", "*" * 10, "Imprimir Ajedrez", "*" * 10)
print("\n")
for i in range(0, f):
    for j in range(0, c):
        print(matrizA[i][j], end=" ")
    print("\n")
