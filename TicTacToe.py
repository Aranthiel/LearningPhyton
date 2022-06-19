
EMPTY = "@"
board = [[EMPTY for i in range(3)] for j in range(3)]
valor=1
for i in range(3):
    for j in range(3):
        board[i][j]=valor
        valor += 1
board[1][1]="X"
    

def DisplayBoard(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    print("+-------+-------+-------+\n|       |       |       |\n|   ", board[0][0], "   |   ", board[0][1], "   |   ", board[0][2], "   |\n|       |       |       |\n+-------+-------+-------+\n|       |       |       |\n|   ", board[1][0], "   |   ", board[1][1], "   |   ", board[1][2], "   |\n|       |       |       |\n+-------+-------+-------+\n|       |       |       |\n|   ", board[2][0], "   |   ", board[2][1], "   |   ", board[2][2], "   |\n|       |       |       |\n+-------+-------+-------+")


def EnterMove(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
    DisplayBoard(board)
    print ("las casillas disponibles son: ")
    MakeListOfFreeFields(board)
    
    fila=int(input("coloca tu ficha, elige una fila: "))
    
    columna= int(input("elige una columna: "))
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    
    not_empty = (board[fila][columna]=="O") or (board[fila][columna]=="X")
    print ("casilla ocupada:", not_empty)
    if not_empty:
        print("la casilla esta ocupada")
        EnterMove(board)
    else:
        board[fila][columna]="O"
    DrawMove(board)


def MakeListOfFreeFields(board):

    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    camposVacios=[]
    print (camposVacios)
    for fila in range(3):
        for columna in range(3):
            if (board[fila][columna]!="O") and (board[fila][columna]!="X"):
                casillaV=[fila,columna]
                camposVacios.append(casillaV)
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    if len(camposVacios)==0:
        print("el juego ha terminado, no quedan movimientos")
        import sys
        sys.exit()
    print (camposVacios)

def VictoryFor(board, sign):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    filaUno = board[0][0]==board[0][1] and board[0][0]==board[0][2]
    filaDos = board[1][0]==board[1][1] and board[1][0]==board[1][2]
    filaTres = board[2][0]==board[2][1] and board[2][0]==board[2][2]
    
    colUno = board[0][0]==board[1][0] and board[0][0]==board[2][0]
    colDos = board[0][1]==board[1][1] and board[0][1]==board[2][1]
    colTres = board[0][2]==board[1][2] and board[0][2]==board[2][2]

    diagUno= board[0][0]==board[1][1] and board[0][0]==board[2][2]
    diagDos= board[0][2]==board[1][1] and board[0][0]==board[2][0]

    if filaUno or filaDos or filaTres or colUno or colDos or colTres or diagUno or diagDos:
        print("el juego ha terminado")
    


def DrawMove(board):
    DisplayBoard(board)
    from random import randrange
    fila=randrange(3)
    print(fila)
    columna=randrange(3)
    print(columna)
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    
    not_empty = (board[fila][columna]=="O") or (board[fila][columna]=="X")
    print(not_empty)
    if not_empty:
        DrawMove(board)
    else:
        board[fila][columna]="X"
    EnterMove(board)

EnterMove(board)
