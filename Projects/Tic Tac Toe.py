class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player = 'X'

    def play(self):
        while not self.game_over():
            self.print_board()
            row, col = self.get_move()
            self.make_move(row, col)
            self.player = 'O' if self.player == 'X' else 'X'
        self.print_board()
        if self.winner() == 'T':
            print("It's a tie!")
        else:
            print(f"{self.winner()} wins!")

    def game_over(self):
        return self.winner() != None

    def winner(self):
        # check rows
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return row[0]

        # check cols
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != ' ':
                return self.board[0][col]

        # check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return self.board[0][2]

        # check for tie
        for row in self.board:
            for col in row:
                if col == ' ':
                    return None
        return 'T'

    def make_move(self, row, col):
        self.board[row][col] = self.player

    def get_move(self):
        while True:
            try:
                row = int(input("Enter row: "))
                col = int(input("Enter col: "))
                if row in range(3) and col in range(3) and self.board[row][col] == ' ':
                    return row, col
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Invalid input, try again.")

    def print_board(self):
        for row in self.board:
            print(row)


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
