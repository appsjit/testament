import random

from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('-----------')
    print(board[7] + '|' + board[8] + '|' + board[9]   )
    print('-|' + '-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|' + '-|-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():
    print("Calling player_input")
    marker =''
    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or O: ').upper()

    if marker =='X':
        return('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):
    board[position] = marker


def win_check(board,mark):
    ## Rows Check
    return ((board[1] ==  board[2] ==  board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark))


def choose_first():
    flip = random.randint(0,1)
    if flip ==0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board,position):
    return board[position] == ''

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    ## Board is Full
    return True


def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('choose position:(1-9)'))

    return position

def replay():
    choice = input("Play Again ? Enter Yes or No")
    return choice == 'Yes'

#test_board = ['#','X','O','X','O','X','O','X','O','X']

#place_marker(test_board,'$',8)
#display_board(test_board)
# display_board(test_board)
# player1_marker, player2_marker = player_input()
# print('Player 1 '+player1_marker)
#place_marker(test_board,'$',8)
#print(win_check(test_board,'X'))

while True:
    the_board =['']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game= input('Ready to Play ? y or n ? ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
            if turn == 'Player 1':
                display_board(the_board)
                #Check a position
                print(turn+' Khelega')
                position = player_choice(the_board)
                # Place marker in position
                place_marker(the_board,player1_marker,position)

                #Check if they won
                if win_check(the_board,player1_marker):
                    display_board(the_board)
                    print('Player 1 has won')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('Tie Game')
                        game_on = False
                    else:
                        turn='Player 2'

            else:
                display_board(the_board)
                print(turn + ' khelo')
                #Check a position
                position = player_choice(the_board)
                # Place marker in position
                place_marker(the_board,player2_marker,position)

                #Check if they won
                if win_check(the_board,player2_marker):
                    display_board(the_board)
                    print('Player 2 has won')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('Tie Game')
                        game_on = False
                    else:
                        turn='Player 1'
                #Or check if there is Tie


                # no Tie No Win Then next player turn


    if not replay():
        break