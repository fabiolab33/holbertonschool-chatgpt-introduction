#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)  # FIX: better board formatting


def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if (board[0][col] == board[1][col] ==
                board[2][col] and board[0][col] != " "):
            return True

    # Check diagonals
    if (board[0][0] == board[1][1] ==
            board[2][2] and board[0][0] != " "):
        return True

    if (board[0][2] == board[1][1] ==
            board[2][0] and board[0][2] != " "):
        return True

    return False


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # FIX: handle invalid input (non-numeric values)
        try:
            row = int(input(
                "Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input(
                "Enter column (0, 1, or 2) for player " + player + ": "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        # FIX: prevent out-of-range input
        if row not in range(3) or col not in range(3):
            print("Invalid position. Please choose 0, 1, or 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        # FIX: check winner BEFORE switching player
        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            break

        # Switch player
        if player == "X":
            player = "O"
        else:
            player = "X"


if __name__ == "__main__":
    tic_tac_toe()