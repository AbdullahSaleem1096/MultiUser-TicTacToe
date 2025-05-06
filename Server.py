import socket
import threading
import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.turn = "X"
        self.you = "X"
        self.opponent = "O"
        self.winner = None
        self.game_over = False
        self.counter = 0

        # Tkinter GUI setup
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe - Host")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.build_gui()

    def build_gui(self):
        for row in range(3):
            for col in range(3):
                btn = tk.Button(self.root, text="", font=("Arial", 20), width=5, height=2,
                                command=lambda r=row, c=col: self.handle_button_click(r, c))
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn

    def handle_button_click(self, row, col):
        if self.you == self.turn and self.board[row][col] == "" and not self.game_over:
            self.board[row][col] = self.you
            self.buttons[row][col].config(text=self.you)
            self.counter += 1
            self.turn = self.opponent
            self.check_game_status()
            self.send_move(row, col)

    def send_move(self, row, col):
        if self.client:
            self.client.send(f"{row},{col}".encode("utf-8"))

    def host_game(self, host, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(1)
        self.client, _ = server.accept()
        threading.Thread(target=self.handle_connection).start()
        self.root.mainloop()

    def handle_connection(self):
        while not self.game_over:
            if self.turn == self.opponent:
                data = self.client.recv(1024).decode("utf-8")
                if data:
                    row, col = map(int, data.split(","))
                    self.board[row][col] = self.opponent
                    self.buttons[row][col].config(text=self.opponent)
                    self.counter += 1
                    self.turn = self.you
                    self.check_game_status()

    def check_game_status(self):
        # Check rows, columns, and diagonals
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != "":
                self.winner = self.board[row][0]
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                self.winner = self.board[0][col]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            self.winner = self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            self.winner = self.board[0][2]

        # Handle game-over scenarios
        if self.winner:
            self.game_over = True
            messagebox.showinfo("Game Over", f"{self.winner} wins!")
            self.root.quit()
        elif self.counter == 9:
            self.game_over = True
            messagebox.showinfo("Game Over", "It's a draw!")
            self.root.quit()


if __name__ == "__main__":
    game = TicTacToe()
    game.host_game("localhost", 9999)
