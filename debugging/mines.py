#!/usr/bin/python3
import random
import os


def clear_screen():
    # FIX: clear_screen must ONLY clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')


# FIX: Minesweeper class must NOT be inside clear_screen()
class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        # FIX: return immediately if mine is hit
        if (y * self.width + x) in self.mines:
            return False

        # FIX: this must execute BEFORE recursive calls
        self.revealed[y][x] = True

        # FIX: recursion must be inside the function
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < self.width and
                            0 <= ny < self.height and
                            not self.revealed[ny][nx]):
                        self.reveal(nx, ny)

        return True

    # Checks if all safe cells are revealed tack 3
    def check_win(self):
        revealed_count = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.revealed[y][x]:
                    revealed_count += 1

        return revealed_count == (self.width * self.height - len(self.mines))

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))

                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break

                # FIX: win condition check
                if self.check_win():
                    self.print_board(reveal=True)
                    print("Congratulations! You've won the game.")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")


# FIX: this block must be OUTSIDE the class
if __name__ == "__main__":
    game = Minesweeper()
    game.play()