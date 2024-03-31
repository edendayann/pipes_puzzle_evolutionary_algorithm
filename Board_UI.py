import tkinter as tk

from Boards import Boards
from Shape import matrix_to_vector_pos, vector_to_matrix_pos


class Board_UI:
    def __init__(self, master, size, game):
        self.master = master
        self.game = game
        if self.game:
            self.frame_moves = tk.Frame(master)
            self.frame_moves.pack(side=tk.TOP, padx=10, pady=5)
            # Moves label
            self.moves = 0
            self.moves_label = tk.Label(self.frame_moves, text="Moves: 0")
            self.moves_label.pack(side=tk.RIGHT)

            self.frame_reset = tk.Frame(master)
            self.frame_reset.pack(side=tk.BOTTOM)
            self.reset_button = tk.Button(self.frame_reset, text="Reset Board", command=self.reset_board)
            self.reset_button.pack(side=tk.BOTTOM, pady=2)

        # Create the puzzle board
        self.canvas = tk.Canvas(master, width=400, height=400, borderwidth=0, relief="ridge")
        self.size = size
        self.cell_size = 396 / self.size
        self.board = Boards(self.size)
        self.shapes = self.board.shapes.split('/')
        self.draw_board()
        self.canvas.pack(side=tk.RIGHT, padx=10, pady=10)
        self.canvas.bind("<Button-1>", self.on_pipe_click)

    def select_board_size(self, event):
        self.size = int(event.widget.get())
        self.board = Boards(self.size)
        self.shapes = self.board.shapes.split('/')
        self.cell_size = 396 / self.size
        self.canvas.delete("all")
        self.draw_board()

    def draw_board(self):
        for row in range(self.size):
            for col in range(self.size):
                orientation = self.board.current[matrix_to_vector_pos((row, col), self.size)]
                self.draw_pipe(col, row, self.shapes[row][col], orientation)

    def on_pipe_click(self, event):
        col = int(event.x // self.cell_size)
        row = int(event.y // self.cell_size)

        self.board.current[matrix_to_vector_pos((row, col), self.size)] += 1
        if self.game:
            self.moves += 1
            self.moves_label.config(text=f"Moves: {self.moves}")
            if self.is_done():
                self.success()
                return

        orientation = self.board.current[matrix_to_vector_pos((row, col), self.size)]
        self.draw_pipe(col, row, self.shapes[row][col], orientation)

    def draw_pipe(self, x, y, shape, orientation):
        fill = "aliceblue"
        outline = "steelblue4"

        pipe_width = self.cell_size / 5  # Width of the pipe shape
        x0 = x * self.cell_size + 2
        y0 = y * self.cell_size + 2
        x1 = x0 + self.cell_size
        y1 = y0 + self.cell_size

        # Calculate points for the center of the cell
        center_x = x0 + self.cell_size / 2
        center_y = y0 + self.cell_size / 2

        # Draw the base cell
        self.canvas.create_rectangle(x0, y0, x1, y1, outline="lightslategray", fill="white")
        orientation %= 4

        if shape == 'l':
            if orientation % 2 == 0:
                self.canvas.create_rectangle(center_x - pipe_width / 2, y0,
                                             center_x + pipe_width / 2, y1, fill=fill, outline=outline)
            else:
                self.canvas.create_rectangle(x0, center_y - pipe_width / 2,
                                             x1, center_y + pipe_width / 2, fill=fill, outline=outline)

        elif shape == 'L':
            if orientation == 0:
                points = [
                    center_x - pipe_width / 2, y0,
                    center_x + pipe_width / 2, y0,
                    center_x + pipe_width / 2, center_y - pipe_width / 2,
                    x1, center_y - pipe_width / 2,
                    x1, center_y + pipe_width / 2,
                    center_x - pipe_width / 2, center_y + pipe_width / 2
                ]
            elif orientation == 1:
                points = [
                    x0, center_y - pipe_width / 2,
                        center_x - pipe_width / 2, center_y - pipe_width / 2,
                        center_x - pipe_width / 2, y0,
                        center_x + pipe_width / 2, y0,
                        center_x + pipe_width / 2, center_y + pipe_width / 2,
                    x0, center_y + pipe_width / 2
                ]
            elif orientation == 2:
                points = [
                    x0, center_y - pipe_width / 2,
                        center_x + pipe_width / 2, center_y - pipe_width / 2,
                        center_x + pipe_width / 2, y1,
                        center_x - pipe_width / 2, y1,
                        center_x - pipe_width / 2, center_y + pipe_width / 2,
                    x0, center_y + pipe_width / 2
                ]
            else:
                points = [
                    center_x - pipe_width / 2, center_y - pipe_width / 2,
                    x1, center_y - pipe_width / 2,
                    x1, center_y + pipe_width / 2,
                    center_x + pipe_width / 2, center_y + pipe_width / 2,
                    center_x + pipe_width / 2, y1,
                    center_x - pipe_width / 2, y1
                ]

            self.canvas.create_polygon(points, fill=fill, outline=outline)

        elif shape == 'i':
            if orientation == 0:
                self.canvas.create_rectangle(center_x - pipe_width / 2, center_y,
                                             center_x + pipe_width / 2, y1, fill=fill, outline=outline)
            elif orientation == 1:
                self.canvas.create_rectangle(center_x, center_y - pipe_width / 2,
                                             x1, center_y + pipe_width / 2, fill=fill, outline=outline)
            elif orientation == 2:
                self.canvas.create_rectangle(center_x - pipe_width / 2, y0,
                                             center_x + pipe_width / 2, center_y, fill=fill, outline=outline)
            else:
                self.canvas.create_rectangle(x0, center_y - pipe_width / 2,
                                             center_x, center_y + pipe_width / 2, fill=fill, outline=outline)

        elif shape == 'T':
            if orientation == 0:
                points = [
                    x0, center_y - pipe_width / 2,
                    x1, center_y - pipe_width / 2,
                    x1, center_y + pipe_width / 2,
                        center_x + pipe_width / 2, center_y + pipe_width / 2,
                        center_x + pipe_width / 2, y1,
                        center_x - pipe_width / 2, y1,
                        center_x - pipe_width / 2, center_y + pipe_width / 2,
                    x0, center_y + pipe_width / 2
                ]
            elif orientation == 1:
                points = [
                    center_x - pipe_width / 2, y0,
                    center_x + pipe_width / 2, y0,
                    center_x + pipe_width / 2, center_y - pipe_width / 2,
                    x1, center_y - pipe_width / 2,
                    x1, center_y + pipe_width / 2,
                    center_x + pipe_width / 2, center_y + pipe_width / 2,
                    center_x + pipe_width / 2, y1,
                    center_x - pipe_width / 2, y1
                ]
            elif orientation == 2:
                points = [
                    x0, center_y - pipe_width / 2,
                        center_x - pipe_width / 2, center_y - pipe_width / 2,
                        center_x - pipe_width / 2, y0,
                        center_x + pipe_width / 2, y0,
                        center_x + pipe_width / 2, center_y - pipe_width / 2,
                    x1, center_y - pipe_width / 2,
                    x1, center_y + pipe_width / 2,
                    x0, center_y + pipe_width / 2
                ]
            else:
                points = [
                    x0, center_y - pipe_width / 2,
                        center_x - pipe_width / 2, center_y - pipe_width / 2,
                        center_x - pipe_width / 2, y0,
                        center_x + pipe_width / 2, y0,
                        center_x + pipe_width / 2, y1,
                        center_x - pipe_width / 2, y1,
                        center_x - pipe_width / 2, center_y + pipe_width / 2,
                    x0, center_y + pipe_width / 2
                ]

            self.canvas.create_polygon(points, fill=fill, outline=outline)

    def reset_board(self):
        if self.game:
            self.moves = 0
            self.moves_label.config(text=f"Moves: {self.moves}")
        self.board.reset_board()
        self.draw_board()

    def is_done(self):
        for i in range(len(self.board.current)):
            pos = vector_to_matrix_pos(i, self.size)
            if self.shapes[pos[0]][pos[1]] == 'l':
                if self.board.current[i] % 2 != self.board.optimal[i]:
                    return False
            if self.board.current[i] % 4 != self.board.optimal[i]:
                return False
        return True

    def success(self):
        # Step 1: Clear the canvas
        self.canvas.delete("all")
        self.master.update_idletasks()

        # Step 2: Add text to the cleared canvas
        text_position_x = self.canvas.winfo_width() / 2
        text_position_y = self.canvas.winfo_height() / 2
        self.canvas.create_text(text_position_x, text_position_y, text="Good Job!", fill="black",
                                font=('Helvetica', 16, 'bold'))
