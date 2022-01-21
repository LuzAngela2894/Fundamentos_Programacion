from random import randrange


def DisplayBoard(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def EnterMove(board):
    ok = False  # suposición falsa - lo necesitamos para entrar en el bucle
    while not ok:
        move = input("Ingresa tu movimiento: ")
        ok = len(move) == 1 and move >= '1' and move <= '9'  # ¿es valido lo que ingreso el usuario?
        if not ok:
            print("Movimiento erróneo, ingrésalo nuevamente")  # no, no lo es. Ingrésalo nuevamente.
            continue
        move = int(move) - 1  # numero de la celda, del 0 al 8
        row = move // 3  # fila de la celda
        col = move % 3  # columna de la celda
        sign = board[row][col]  # marca el cuadro elegido
        ok = sign not in ['O', 'X']
        if not ok:  # esta ocupado, ingresa una posición nuevamente
            print("¡Campo ocupado, ingresa nuevamente!")
            continue
    board[row][col] = 'O'  # colocar '0' al cuadro seleccionado


def MakeListOfFreeFields(board):
    free = []  # la lista esta vacía inicialmente
    for row in range(3):  # itera a través de las filas
        for col in range(3):  # itera a través de las columnas
            if board[row][col] not in ['O', 'X']:  # ¿Está la celda libre?
                free.append((row, col))  # si, agrega una nueva tupla a la lista
    return free


def VictoryFor(board, sgn):
    if sgn == "X":  # ¿Estamos buscando X?
        who = 'yo'  # Si, es la maquina
    elif sgn == "O":  # ... o estamos buscando O?
        who = 'tu'  # Si, es el usuario
    else:
        who = None  # ¡No debemos de caer aquí!
    cross1 = cross2 = True  # para las diagonales
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:  # revisar filas rc
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:  # revisar columnas rc
            return who
        if board[rc][rc] != sgn:  # revisar la primer diagonal
            cross1 = False
        if board[2 - rc][2 - rc] != sgn:  # revisar la segunda diagonal
            cross2 = False
    if cross1 or cross2:
        return who
    return None


def DrawMove(board):
    free = MakeListOfFreeFields(board)  # hace una lista de los cuadros vacios o libres
    cnt = len(free)
    if cnt > 0:  # si la lista no esta vacía, elegir un lugar para 'X' y colocarla
        this = randrange(cnt)
        row, col = free[this]
        board[row][col] = 'X'


board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]  # crear un tablero vacío
board[1][1] = 'X'  # colocar la primer 'X' en el centro
free = MakeListOfFreeFields(board)
humanturn = True  # ¿De quien es turno ahora?
while len(free):
    DisplayBoard(board)
    if humanturn:
        EnterMove(board)
        victor = VictoryFor(board, 'O')
    else:
        DrawMove(board)
        victor = VictoryFor(board, 'X')
    if victor != None:
        break
    humanturn = not humanturn
    free = MakeListOfFreeFields(board)

DisplayBoard(board)
if victor == 'tu':
    print("¡Has ganado!")
elif victor == 'yo':
    print("¡He ganado!")
else:
    print("¡Empate!")
