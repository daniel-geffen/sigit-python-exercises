"""
This module determines the outcome of a tic-tac-toe game and displays is to the user.
"""

game = [
    [1, 2, 0],
    [2, 1, 0],
    [2, 1, 1]
]


def create_winning_options():
    """
    Creates a list of the trios that a player can win with.
    :return: A list of trios, with the value that is in that cell on the board.
    """
    winning_options = []
    winning_options += [[game[i][j] for j in range(3)] for i in range(3)]  # Rows
    winning_options += [[game[j][i] for j in range(3)] for i in range(3)]  # Cols
    winning_options.append([game[i][i] for i in range(3)])  # Primary Diagonal
    winning_options.append([game[i][2 - i] for i in range(3)])  # Secondary Diagonal
    return winning_options


def check_winner(winning_options):
    """
    Prints the outcome of the game, by checking all the winning options.
    If a winner is not found, a tie is displayed.
    :param winning_options: A list of trios that a player can win with.
    """
    for option in winning_options:
        if all(x != 0 and x == option[0] for x in option):
            print(f"Player {option[0]} won the game!")
            return
    print("The game ended with a tie")


def main():
    winning_options = create_winning_options()
    check_winner(winning_options)


if __name__ == '__main__':
    main()
