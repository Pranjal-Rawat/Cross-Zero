import tkinter as tk
from tkinter import messagebox

def ConstBoard():
    for i in range(0, 9):
        x = i % 3
        y = i // 3
        if board[i] == 0:
            canvas.create_rectangle(x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size, fill="white", outline="black")
        elif board[i] == -1:
            canvas.create_text((x + 0.5) * cell_size, (y + 0.5) * cell_size, text="X", font=("Helvetica", cell_size // 2), fill="black")
        elif board[i] == 1:
            canvas.create_text((x + 0.5) * cell_size, (y + 0.5) * cell_size, text="O", font=("Helvetica", cell_size // 2), fill="black")

def User1Turn(event):
    global board
    pos_x = event.x // cell_size
    pos_y = event.y // cell_size
    pos = pos_y * 3 + pos_x
    if board[pos] != 0:
        messagebox.showerror("Error", "Wrong Move")
        return
    board[pos] = -1
    ConstBoard()
    if analyzeboard(board) != 0:
        game_over()
    else:
        Compturn()

def Compturn():
    global board
    pos = -1
    value = -2
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = 1
            score = -minmax(board, -1)
            board[i] = 0
            if score > value:
                value = score
                pos = i
    board[pos] = 1
    ConstBoard()
    if analyzeboard(board) != 0:
        game_over()

def analyzeboard(board):
    cb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(0, 8):
        if board[cb[i][0]] != 0 and board[cb[i][0]] == board[cb[i][1]] and board[cb[i][0]] == board[cb[i][2]]:
            return board[cb[i][0]]
    if 0 not in board:
        return 2  # Draw
    return 0

def game_over():
    winner = analyzeboard(board)
    if winner == -1:
        messagebox.showinfo("Game Over", "Player X Wins!!! O Loses!!")
    elif winner == 1:
        messagebox.showinfo("Game Over", "Player O Wins!!! X Loses!!")
    else:
        messagebox.showinfo("Game Over", "Draw!")

def minmax(board, player):
    x = analyzeboard(board)
    if x != 0:
        return player * x
    pos = -1
    value = -2
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = player
            score = -minmax(board, -player)
            board[i] = 0
            if score > value:
                value = score
                pos = i
    if pos == -1:
        return 0
    return value

root = tk.Tk()
cell_size = 100  # Size of each cell in the grid
canvas = tk.Canvas(root, width=3 * cell_size, height=3 * cell_size)
canvas.pack()

board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
ConstBoard()
canvas.bind("<Button-1>", User1Turn)

root.mainloop()

