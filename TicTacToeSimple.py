import random

#Primero defino la forma del tablero
def tablero(board):

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

#Que el primer jugador decida si quiere ser X o O

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('¿El primer jugador quiere ser X o O?\n').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker

#Defino cómo se puede ganar el juego

def ganar(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # Forma Diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # Forma Diagonal

#Pongo a que se seleccione aleatoreamente el primer jugador
    
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Jugador 2'
    else:
        return 'Jugador 1'

def space_check(board, position):
    
    return board[position] == ' '



def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


#Dónde el jugador quiere hacer su jugada
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Selecciona dónde quieres jugar (1-9) \n'))
        
    return position

#En caso de querer repetir el juego coloco un replay

def replay():
    
    input('¿Quieres jugar de nuevo? Presiona y para jugar de nuevo. Si no quieres jugar de nuevo presiona enter.\n').lower().startswith('y')
  
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

print('¡Bienvenido al juego!\n\n')

print('Este es el tablero, \n  cada número es dónde debes colocar tu movimiento \n\n')
#Para tener en claro cómo es exactamente el tablero y que no haya confusión durante el juego lo coloque para que vean qué numero equivale a cada posición

movimientos = ['#','1','2','3','4','5','6','7','8','9']
tablero(movimientos)

print('\n')

while True:
   
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' empezará el juego.')
    
    play_game = input('Presiona y para empezar el juego . . .\n')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    


    while game_on:
        if turn == 'Jugador 1':
            # Turno del jugador 1
            
            tablero(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if ganar(theBoard, player1_marker):
                tablero(theBoard)
                print('¡Felicitaciones! Has ganado el juego. Mal por ti, jugador 2')
                game_on = False
            else:
                if full_board_check(theBoard):
                    tablero(theBoard)
                    print('Los dos pierden. Mentira, es un empate que es casi como perder')
                    break
                else:
                    turn = 'Jugador 2'

        else:
            # Turno del jugador 2
            
            tablero(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if ganar(theBoard, player2_marker):
                tablero(theBoard)
                print('¡Felicitaciones! Has ganado el juego. Mal por ti, jugador 1')
                game_on = False
            else:
                if full_board_check(theBoard):
                    tablero(theBoard)
                    print('Los dos pierden. Mentira, es un empate que es casi como perder')
                    break
                else:
                    turn = 'Jugador 1'

    if not replay():
        break

