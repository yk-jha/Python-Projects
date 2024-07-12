# Tic Tac Toe

# Create the game board
board = [' ' for _ in range(9)]

# Function to print the game board
def print_board():
    print("-------------")
    for i in range(3):
        print("|", board[i * 3], "|", board[i * 3 + 1], "|", board[i * 3 + 2], "|")
        print("-------------")

# Function to check for a winner
def check_winner():
    # Check rows
    for i in range(3):
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != ' ':
            return board[i * 3]

    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return board[i]

    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] != ' ':
        return board[2]

    # No winner
    return None

# Function to check if the board is full
def is_board_full():
    return ' ' not in board

# Function to play the game
def play_game():
    print("Welcome to Tic Tac Toe!")
    print_board()
    current_player = 'X'

    while True:
        print("It's", current_player, "'s turn.")
        position = int(input("Enter a position (1-9): ")) - 1

        if position < 0 or position > 8:
            print("Invalid position. Try again.")
            continue

        if board[position] != ' ':
            print("Position already taken. Try again.")
            continue

        board[position] = current_player
        print_board()

        winner = check_winner()
        if winner:
            print("Congratulations!", winner, "wins!")
            break

        if is_board_full():
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()
