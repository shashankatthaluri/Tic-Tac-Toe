import sys
import colorama
from colorama import Fore, Back, Style
import random

ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
X, O, BLANK = 'X', 'O', ' '  # Constants for string values.

colorama.init(autoreset=True)  # Initialize colorama

def main():
    print('Welcome to Tic-Tac-Toe!')
    game_board = get_blank_board()  # Create a TTT board dictionary.
    num_players = get_number_of_players()
    player1_name = input('Enter the name for Player 1: ')
    player2_name = input('Enter the name for Player 2: ') if num_players == 2 else 'Computer'

    current_player, next_player = X, O  # X goes first, O goes next.

    while True:  # Main game loop.
        # Display the board on the screen:
        print(get_board_str(game_board))

        # Keep asking the player until they enter a number 1-9:
        move = get_player_move(current_player, game_board, num_players, player1_name, player2_name)
        if move == 'QUIT':
            print(Fore.RED + 'Thanks for playing!')
            sys.exit()

        update_board(game_board, move, current_player)  # Make the move.

        # Check if the game is over:
        if is_winner(game_board, current_player):  # Check for a winner.
            print_game_result(game_board, player=current_player, player1_name=player1_name, player2_name=player2_name)
            break
        elif is_board_full(game_board):  # Check for a tie.
            print_game_result(game_board, tie=True, player1_name=player1_name, player2_name=player2_name)
            break
        # Switch turns to the next player:
        current_player, next_player = next_player, current_player
    print(Fore.YELLOW + 'Thanks for playing!')


def get_blank_board():
    """Create a new, blank tic-tac-toe board."""
    # Map of space numbers: 1 | 2 | 3
    #                       ---|---|---
    #                       4 | 5 | 6
    #                       ---|---|---
    #                       7 | 8 | 9
    # Keys are 1 through 9, the values are X, O, or BLANK:
    board = {space: BLANK for space in ALL_SPACES}  # All spaces start as blank.
    return board


def get_board_str(board):
    """Return a text-representation of the board."""
    return '''
       {} | {} | {}  1 2 3
      ---|---|---
       {} | {} | {}  4 5 6
      ---|---|---
       {} | {} | {}  7 8 9'''.format(
        colorize(board['1']),
        colorize(board['2']),
        colorize(board['3']),
        colorize(board['4']),
        colorize(board['5']),
        colorize(board['6']),
        colorize(board['7']),
        colorize(board['8']),
        colorize(board['9'])
    )


def colorize(cell):
    """Colorize the cell based on the player."""
    if cell == 'X':
        return Fore.GREEN + cell
    elif cell == 'O':
        return Fore.BLUE + cell
    else:
        return cell


def get_number_of_players():
    """Ask the user for the number of players."""
    while True:
        num_players = input('Enter the number of players (1 or 2): ')
        if num_players in {'1', '2'}:
            return int(num_players)
        else:
            print('Invalid input. Please enter 1 or 2.')


def get_player_move(player, board, num_players, player1_name, player2_name):
    """Ask the current player for their move."""
    if player == X or num_players == 2:
        while True:
            print('Enter your move, {} (1-9), or type QUIT to quit:'.format(player1_name if player == X else player2_name))
            move = input('> ').upper()
            if move == 'QUIT':
                return 'QUIT'
            elif move in ALL_SPACES and is_valid_space(board, move):
                return move
            else:
                print('Invalid move. Please enter a number 1-9.')
    else:
        # Computer's move (player2)
        available_moves = [space for space in ALL_SPACES if is_valid_space(board, space)]
        return random.choice(available_moves)


def is_valid_space(board, space):
    """Returns True if the space on the board is a valid space number
    and the space is blank."""
    return space in ALL_SPACES and board[space] == BLANK


def is_winner(board, player):
    """Return True if player is a winner on this TTTBoard."""
    # Shorter variable names used here for readablility:
    b, p = board, player
    # Check for 3 marks across 3 rows, 3 columns, and 2 diagonals.
    return ((b['1'] == b['2'] == b['3'] == p) or  # Across top
            (b['4'] == b['5'] == b['6'] == p) or  # Across middle
            (b['7'] == b['8'] == b['9'] == p) or  # Across bottom
            (b['1'] == b['4'] == b['7'] == p) or  # Down left
            (b['2'] == b['5'] == b['8'] == p) or  # Down middle
            (b['3'] == b['6'] == b['9'] == p) or  # Down right
            (b['3'] == b['5'] == b['7'] == p) or  # Diagonal
            (b['1'] == b['5'] == b['9'] == p))    # Diagonal


def is_board_full(board):
    """Return True if every space on the board has been taken."""
    return all(board[space] != BLANK for space in ALL_SPACES)


def update_board(board, space, mark):
    """Sets the space on the board to mark."""
    board[space] = mark


def print_game_result(board, player=None, tie=False, player1_name=None, player2_name=None):
    """Print the result of the game."""
    print(get_board_str(board))
    if tie:
        print('The game is a tie!')
    else:
        winner_name = player1_name if player == X else player2_name
        winner_color = Fore.GREEN if player == X else Fore.BLUE
        print(winner_color + '{} has won the game!'.format(winner_name))


if __name__ == '__main__':
    main()  # Call main() if this module is run, but not when imported.
