import tkinter as tk
from tkinter import ttk


class PipesPuzzleUI:
    def __init__(self, master, main_function):
        self.master = master
        self.main_function = main_function
        self.master.title("Pipes Puzzle Simulator")

        # Create the puzzle board
        self.canvas = tk.Canvas(self.master, width=700, height=500, borderwidth=2, relief="ridge")
        self.canvas.pack(side=tk.RIGHT, padx=10, pady=10)

        # board size frame
        self.frame_board_size = tk.Frame(self.master)
        self.frame_board_size.pack(padx=10, pady=10, anchor="w")
        self.label_board_size = tk.Label(self.frame_board_size, text="Choose board size:", anchor="w")
        self.label_board_size.pack(side=tk.LEFT, padx=5)
        self.value_board_size = ttk.Combobox(self.frame_board_size, values=["4", "5", "7"], width=5)
        self.value_board_size.set("4")
        self.value_board_size.pack(side=tk.LEFT)
        self.value_board_size.bind("<<ComboboxSelected>>", self.select_board_size)

        # population size frame
        self.frame_population_size = tk.Frame(self.master)
        self.frame_population_size.pack(padx=10, pady=10, anchor="w")
        self.label_population_size = tk.Label(self.frame_population_size, text="Population Size:", anchor="w")
        self.label_population_size.pack(side=tk.LEFT, padx=(0, 5))
        self.value_population_size = tk.Scale(self.frame_population_size, from_=50, to=500, orient=tk.HORIZONTAL,
                                              showvalue=True)
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
        self.value_is_moves.pack(side=tk.LEFT, padx=(0, 5))
        self.value_is_moves.bind("<<ComboboxSelected>>", self.show_scale)  # Bind event to show scale
        # moves range frame
        self.frame_moves_range = tk.Frame(self.master)
        self.frame_moves_range.pack_forget()
        self.label_moves_range = tk.Label(self.frame_moves_range, text="Moves Range:", anchor="w")
        self.label_moves_range.pack_forget()  # Hide initially
        self.value_moves_range = tk.Scale(self.frame_moves_range, from_=0, to=50, orient=tk.HORIZONTAL, showvalue=True)
        self.value_moves_range.set(4)
        self.value_moves_range.pack_forget()  # Hide initially

        # Submit button
        self.submit_button = tk.Button(self.master, text="Submit", command=self.handle_submit)
        self.submit_button.pack(side=tk.BOTTOM, pady=10)

    def select_board_size(self, event):
        value = self.value_board_size.get()
        # Process the selected value (you can add your logic here)
        print("Selected value:", value)

    def show_scale(self, event=None):
        # Show scale when a value is selected in combobox
        value = self.value_is_moves.get()
        if value == "Yes":
            self.frame_moves_range.pack(padx=10, pady=10, anchor="w")
            self.label_moves_range.pack(side=tk.LEFT, padx=(0, 5))
            self.value_moves_range.pack(side=tk.LEFT, padx=(0, 5))
        if value == "No":
            self.frame_moves_range.pack_forget()
            self.label_moves_range.pack_forget()
            self.value_moves_range.pack_forget()

    def handle_submit(self):
        board_size = int(self.value_board_size.get())
        is_moves = self.value_is_moves.get() == "Yes"
        moves_range = self.value_moves_range.get()
        population_size = self.value_population_size.get()
        elitism_rate = self.value_elitism_rate.get()
        max_generation = self.value_max_generation.get()
        self.main_function(board_size=board_size, is_moves=is_moves, moves_range=moves_range,
                           population_size=population_size, elitism_rate=elitism_rate, max_generation=max_generation)
