import tkinter as tk
from tkinter import ttk

from Board_UI import Board_UI


class PipesPuzzleUI:
    def __init__(self, master, main_function):
        self.i = 0
        self.master = master
        self.main_function = main_function
        self.master.title("Pipes Puzzle Simulator")
        self.best_sol = []
        # self.master.configure(background="white")

        self.board = Board_UI(self.master, 4, False)

        # board size frame
        self.frame_board_size = tk.Frame(self.master)
        self.frame_board_size.pack(padx=10, pady=10, anchor="w")
        self.label_board_size = tk.Label(self.frame_board_size, text="Choose board size:", anchor="w")
        self.label_board_size.pack(side=tk.LEFT, padx=(0, 5))
        self.value_board_size = ttk.Combobox(self.frame_board_size, values=["4", "5", "7", "10"], width=5)
        self.value_board_size.set("4")
        self.value_board_size.pack(side=tk.LEFT, padx=(0, 5))
        self.value_board_size.bind("<<ComboboxSelected>>", self.board.select_board_size)

        # population size frame
        self.frame_population_size = tk.Frame(self.master)
        self.frame_population_size.pack(padx=10, pady=10, anchor="w")
        self.label_population_size = tk.Label(self.frame_population_size, text="Population Size:", anchor="w")
        self.label_population_size.pack(side=tk.LEFT, padx=(0, 5))
        self.value_population_size = tk.Scale(self.frame_population_size, from_=50, to=500, orient=tk.HORIZONTAL,
                                              showvalue=True, resolution=2)
        self.value_population_size.set(100)
        self.value_population_size.pack(side=tk.LEFT, padx=(0, 5))

        # elitism rate frame
        self.frame_elitism_rate = tk.Frame(self.master)
        self.frame_elitism_rate.pack(padx=10, pady=10, anchor="w")
        self.label_elitism_rate = tk.Label(self.frame_elitism_rate, text="Elitism Rate:", anchor="w")
        self.label_elitism_rate.pack(side=tk.LEFT, padx=(0, 5))
        self.value_elitism_rate = tk.Scale(self.frame_elitism_rate, from_=0.0, to=1.0, orient=tk.HORIZONTAL,
                                           showvalue=True, resolution=0.01)
        self.value_elitism_rate.set(0.05)
        self.value_elitism_rate.pack(side=tk.LEFT, padx=(0, 5))

        # max generation frame
        self.frame_max_generation = tk.Frame(self.master)
        self.frame_max_generation.pack(padx=10, pady=10, anchor="w")
        self.label_max_generation = tk.Label(self.frame_max_generation, text="Max Generation:", anchor="w")
        self.label_max_generation.pack(side=tk.LEFT, padx=(0, 5))
        self.value_max_generation = tk.Scale(self.frame_max_generation, from_=0, to=500, orient=tk.HORIZONTAL,
                                             showvalue=True)
        self.value_max_generation.set(50)
        self.value_max_generation.pack(side=tk.LEFT, padx=(0, 5))

        # moves frame
        self.frame_is_moves = tk.Frame(self.master)
        self.frame_is_moves.pack(padx=10, pady=10, anchor="w")
        self.label_is_moves = tk.Label(self.frame_is_moves, text="Activate Moves Mode:", anchor="w")
        self.label_is_moves.pack(side=tk.LEFT, padx=(0, 5))
        self.value_is_moves = ttk.Combobox(self.frame_is_moves, values=["Yes", "No"], width=5)
        self.value_is_moves.set("No")
        self.value_is_moves.pack(side=tk.LEFT, padx=(0, 5))
        self.value_is_moves.bind("<<ComboboxSelected>>", self.show_scale)  # Bind event to show scale
        # moves range frame
        self.frame_moves_range = tk.Frame(self.master)
        self.frame_moves_range.pack_forget()
        self.label_moves_range = tk.Label(self.frame_moves_range, text="Moves Range:", anchor="w")
        self.label_moves_range.pack(side=tk.LEFT, padx=(0, 5))
        self.value_moves_range = tk.Scale(self.frame_moves_range, from_=0, to=50, orient=tk.HORIZONTAL, showvalue=True)
        self.value_moves_range.set(4)
        self.value_moves_range.pack(side=tk.LEFT, padx=(0, 5))

        # submit and play game buttons
        self.frame_bottom = tk.Frame(self.master)
        self.frame_bottom.pack(side=tk.BOTTOM)
        self.submit_button = tk.Button(self.frame_bottom, text="Start Algorithm", command=self.handle_submit)
        self.submit_button.pack(side=tk.LEFT, padx=5)
        self.play_game_button = tk.Button(self.frame_bottom, text="Play Game", command=self.play_game)
        self.play_game_button.pack(side=tk.LEFT, pady=2)

        self.frame_finish = tk.Frame(self.master)
        self.frame_finish.pack(side=tk.BOTTOM)
        self.display_solution_button = tk.Button(self.frame_finish, text="Display Best Solution",
                                                 command=self.display_solution, state=tk.DISABLED)
        self.display_solution_button.pack(side=tk.LEFT, padx=5)
        self.reset_solution_button = tk.Button(self.frame_finish, text="Reset Board", command=self.board.reset_board)
        self.reset_solution_button.pack(side=tk.LEFT, pady=2)

        self.frame_label_finish = tk.Frame(self.master)
        self.frame_label_finish.pack(side=tk.BOTTOM, fill="x")
        self.finish_text = tk.StringVar()
        self.label_finish = tk.Label(self.frame_label_finish, textvariable=self.finish_text, anchor="w",
                                     justify=tk.LEFT)
        self.label_finish.pack(side=tk.BOTTOM, fill="x")

    def show_scale(self, event=None):
        # Show scale when a value is selected in combobox
        value = self.value_is_moves.get()
        if value == "Yes":
            self.frame_moves_range.pack(padx=10, pady=10, anchor="w")
        if value == "No":
            self.frame_moves_range.pack_forget()

    def handle_submit(self):
        self.finish_text.set("Loading...")
        self.master.update_idletasks()

        board_size = int(self.value_board_size.get())
        is_moves = self.value_is_moves.get() == "Yes"
        moves_range = self.value_moves_range.get()
        population_size = self.value_population_size.get()
        elitism_rate = self.value_elitism_rate.get()
        max_generation = self.value_max_generation.get()
        output_file = open(f"output/{self.i}.size={board_size}", "w")
        output_file.write(f"#{self.i} run\nboard_size = {board_size}\n"
                          f"is_moves = {is_moves}\nmoves_range = {moves_range}\n"
                          f"population_size = {population_size}\nelitism_rate = {elitism_rate}\n"
                          f"max_generation = {max_generation}\n\n")
        print(f"created output file- {self.i}.size={board_size}, starting algorithm...")
        self.best_sol, best_score, time = self.main_function(board_size=board_size, is_moves=is_moves,
                                                             moves_range=moves_range,
                                                             population_size=population_size,
                                                             elitism_rate=elitism_rate,
                                                             max_generation=max_generation,
                                                             output_file=output_file)
        self.i += 1

        self.finish_text.set(f"Evolutionary algorithm done in {time} seconds,\n best fitness score= {best_score}/10.")
        self.display_solution_button['state'] = tk.NORMAL

    def play_game(self):
        root = tk.Tk()
        root.title("Pipes Puzzle Game")
        board_size = int(self.value_board_size.get())
        game = Board_UI(root, board_size, True)

        def on_close():
            # game.clean_up()  # Call the cleanup method of your Board_UI instance
            root.after(100, root.destroy)

        root.protocol("WM_DELETE_WINDOW", on_close)
        root.mainloop()

    def display_solution(self):
        self.board.board.current = self.best_sol
        self.board.draw_board()
