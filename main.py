import os

board = {
    1: '1', 2: '2', 3: '3',
    4: '4', 5: '5', 6: '6',
    7: '7', 8: '8', 9: '9',
}

player_1_moves = 0
player_2_moves = 0
player_1_turn = True
# print(board)


# player 1:
player_1_score = 0


def player_1():
    global player_1_score, player_1_turn, player_1_moves
    for step in board:
        if step == move:
            if board[step] != 'O' and board[step] != 'X':
                board[step] = 'X'
                player_1_turn = False
                print('Player 2, Your Turn!')
            else:
                print('Move already taken')
                player_1_turn = True
                print('Player 1, Make a Proper Move!')


# player 2
player_2_score = 0


def player_2():

    global player_2_score, player_1_turn, player_2_moves
    for step in board:
        if step == move:
            if board[step] != 'O' and board[step] != 'X':
                board[step] = 'O'
                player_1_turn = True
                print('Player 1, Your Turn!')
            else:
                print('Move already taken')
                player_1_turn = False
                print('Player 2, Make a Proper Move!')


def live_board():
    print(f'   {board[1]}  | {board[2]}  | {board[3]} \n'
          f'________________\n'
          f'   {board[4]}  | {board[5]}  | {board[6]} \n'
          f'________________\n'
          f'   {board[7]}  | {board[8]}  | {board[9]} \n'
          )


print('First time hearing about this Game? Worry Not! Rules here: '
      'https://www.exploratorium.edu/explore/puzzles/tictactoe#:~:'
      'text=Rules%20for%20Tic-Tac-Toe%201%20The%20game%20is%20played,squares%20ar'
      'e%20full%2C%20the%20game%20is%20over.%20')
print("\n")
print('Welcome to my TicTac version. You should know the rules!')
print("\n")

if player_1_turn:
    print('Player 1, Your Turn!')
live_board()

active = True
while active:
    try:
        move = int(input('Enter your move: '))
        if move <= 9:
            if player_1_turn:
                player_1()
            else:
                player_2()

            live_board()

        else:
            print('You shot beyond our limit! Try again with a digit less than 10.')
    except ValueError:
        print('Please enter a digit. Letters are not allowed!')
