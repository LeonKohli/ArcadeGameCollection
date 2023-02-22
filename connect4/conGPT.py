import os

# Define the game board
board = [[' ' for i in range(7)] for j in range(6)]

# Function to print the board
def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('╔' + '═'*29 + '╗')
    for row in range(6):
        print('║ ', end='')
        for col in range(7):
            print(board[row][col] + ' │ ', end='')
        print('\n' + ('╠' if row < 5 else '╚') + '═'*29 + ('╣' if row < 5 else '╝'))

# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for row in range(6):
        for col in range(4):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                return True
    # Check columns
    for col in range(7):
        for row in range(3):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                return True
    # Check diagonals
    for row in range(3):
        for col in range(4):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                return True
    for row in range(3, 6):
        for col in range(4):
            if board[row][col] == player and board[row-1][col+1] == player and board[row-2][col+2] == player and board[row-3][col+3] == player:
                return True
    # If no win conditions are met, return False
    return False

# Function to check if the game is a draw
def check_draw(board):
    for row in range(6):
        for col in range(7):
            if board[row][col] == ' ':
                return False
    return True

# Main game loop
player = 'X'
while True:
    # Print the board
    print_board(board)

    # Get the player's move
    while True:
        try:
            col = int(input("Player " + player + ", choose a column (1-7): ")) - 1
            if col < 0 or col > 6:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")

    # Place the player's piece on the board
    for row in range(5, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player
            break

    # Check if the player has won
    if check_win(board, player):
        print_board(board)
        print("Player " + player + " wins!")
        break

    # Check if the game is a draw
    if check_draw(board):
        print_board(board)
        print("The game is a draw.")
        break

    # Switch to the other player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
        
