import random
import time
import copy
import os

HEIGHT = 30
WIDTH = 60
GENERATIONS = 1000

# Create a random initial state
def create_board():
    board = []
    for i in range(HEIGHT):
        row = []
        for j in range(WIDTH):
            if random.random() > 0.5:
                row.append('X')
            else:
                row.append('.')
        board.append(row)
    return board

#define a function to clear the terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Print the current state of the board
def print_board(board):
    clear()
    output = ''
    for i in range(HEIGHT):
        for j in range(WIDTH):
            output += board[i][j]
        output += '\n'
    print(output)

# Compute the next state of the board
def next_board(board):
    new_board = copy.deepcopy(board)
    for i in range(HEIGHT):
        for j in range(WIDTH):
            count = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if k == 0 and l == 0:
                        continue
                    row = (i + k + HEIGHT) % HEIGHT
                    col = (j + l + WIDTH) % WIDTH
                    if board[row][col] == 'X':
                        count += 1
            if board[i][j] == 'X' and (count < 2 or count > 3):
                new_board[i][j] = '.'
            elif board[i][j] == '.' and count == 3:
                new_board[i][j] = 'X'
    return new_board

# Run the simulation
def run():
    board = create_board()
    print_board(board)
    for i in range(GENERATIONS):
        board = next_board(board)
        print_board(board)

if __name__ == '__main__':
    run()
