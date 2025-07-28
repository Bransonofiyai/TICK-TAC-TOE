class Option:
    """Represents a player's symbol (X or O)."""
    def __init__(self, symbol):
        if symbol not in ('X', 'O'):
            raise ValueError("Option must be 'X' or 'O'")
        self.symbol = symbol

    def __str__(self):
        return self.symbol
 

class Table:
    """Represents the 3x3 grid, manages cell states, and provides methods to update and display the board."""
    def __init__(self):
        self.grid = [[None for _ in range(3)] for _ in range(3)]

    def display(self):
        print("  0 1 2")
        for i, row in enumerate(self.grid):
            row_display = f"{i} " + "|".join([cell.symbol if cell else ' ' for cell in row])
            print(row_display)
            if i < 2:
                print("  -----")

    def is_empty(self, row, col):
        return self.grid[row][col] is None

    def place(self, row, col, option):
        if not (0 <= row < 3 and 0 <= col < 3):
            raise ValueError("Row and column must be between 0 and 2.")
        if not self.is_empty(row, col):
            raise ValueError("The selected cell is not empty!")
        self.grid[row][col] = option

    def is_full(self):
        return all(cell is not None for row in self.grid for cell in row)

    def check_winner(self):
        # Check rows, columns, and diagonals
        lines = self.grid + [list(col) for col in zip(*self.grid)]
        lines.append([self.grid[i][i] for i in range(3)])
        lines.append([self.grid[i][2 - i] for i in range(3)])
        for line in lines:
            if line[0] and all(cell == line[0] for cell in line):
                return line[0].symbol
        return None


class Match:
    """Represents a single game session, manages turns, checks for a winner or draw."""
    def __init__(self):
        self.table = Table()
        self.players = [Option('X'), Option('O')]
        self.current = 0  # Index of current player

    def play(self):
        print("Welcome to Tic Tac Toe!")
        while True:
            self.table.display()
            player = self.players[self.current]
            print(f"Player {player}, enter your move (row and column): ", end='')
            try:
                move = input().strip().split()
                if len(move) != 2:
                    raise ValueError("Please enter two numbers (row and column).")
                row, col = map(int, move)
                self.table.place(row, col, player)
            except Exception as e:
                print(f"[ERROR] {e}")
                continue
            winner = self.table.check_winner()
            if winner:
                self.table.display()
                print(f"Player {winner} wins!")
                break
            if self.table.is_full():
                self.table.display()
                print("It's a draw!")
                break
            self.current = 1 - self.current


if __name__ == "__main__":
    Match().play()
