
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author : Radim Novotný
email: r.novotny@centrum.cz
"""

def tic_tac_toe():
    print("Welcome to Tic Tac Toe")
    print("============================================")
    print("GAME RULES:")
    print("Each player can place one mark (or stone)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print("============================================")
    print("Let's start the game")
    print("--------------------------------------------")

def display_game_board(board):
    print("+---+---+---+")
    for line in board:
        print(f"| {line[0]} | {line[1]} | {line[2]} |")
        print("+---+---+---+")
    print("============================================")

def evaluate_the_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(board[i][j] in ('X', 'O') for i in range(3) for j in range(3))

def player_move(board, player):
    while True:
        try:
            print(f"Player {player.lower()} | Please enter your move number: ", end='')
            move = int(input()) - 1
            line, column = divmod(move, 3)
            if move < 0 or move >= 9:
                print("Invalid choice. Please enter a number between (1-9):")
            elif board[line][column] in ('X', 'O'):
                print("This field is already taken! Please choose another one.")
            else:
                board[line][column] = player
                break
        except ValueError:
            print("Invalid choice. Please enter a number between (1-9):")

def main():
    tic_tac_toe()
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    current_player = 'X'
    while True:
        display_game_board(board)
        player_move(board, current_player)
        if evaluate_the_win(board, current_player):
            display_game_board(board)
            print(f"Congratulations, the player {current_player.lower()} WON!")
            print("============================================")
            break
        if is_draw(board):
            display_game_board(board)
            print("It's a DRAW! The playing field is full.")
            print("============================================")
            break
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()