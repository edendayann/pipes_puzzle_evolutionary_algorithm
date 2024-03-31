import matplotlib.pyplot as plt

from main import start_algorithm


class Information:
    """class for graph ploting"""

    def __init__(self, file_name):
        self.file_name = file_name
        self.all_best_fitness = []
        self.all_worst_fitness = []
        self.all_average_fitness = []
        self.num_of_gens = []
        self.best_fitness = 0

    def read_file(self):
        with open(self.file_name, "r") as my_file:
            lines = my_file.readlines()
            # print(*lines)
            for i in range(0, len(lines), 6):
                if i >= len(lines) - 2:
                    return
                num_of_gen = int(lines[i][12:].strip())
                self.num_of_gens.append(num_of_gen)
                best_fitness = float(lines[i + 2][13:].strip())
                self.all_best_fitness.append(best_fitness)
                worst_fitness = float(lines[i + 3][14:].strip())
                self.all_worst_fitness.append(worst_fitness)
                average_fitness = float(lines[i + 4][16:].strip())
                self.all_average_fitness.append(average_fitness)

    def plot_graph(self, title):
        # x axis values
        x = self.num_of_gens
        # corresponding y axis values
        y1 = self.all_best_fitness
        y2 = self.all_worst_fitness
        y3 = self.all_average_fitness

        # plotting the points
        plt.plot(x, y1, color='blue', label="Best Fitness")
        plt.plot(x, y2, color='red', label="Worst Fitness")
        plt.plot(x, y3, color='green', label="Average Fitness")

        # naming the x
        plt.xlabel('Number of generations')
        # naming the y
        plt.ylabel('Fitness values')

        # giving a title to my graph
        plt.title(title)

        # show a legend on the plot
        plt.legend()

        # function to show the plot
        plt.show()


def main():
    output_file = open(f"generation_mutation_prob=0.7.txt", "w")
    start_algorithm(board_size=5, is_moves=False, population_size=50, mutation_prob=0.7,
                    elitism_rate=0.05, max_generation=300, output_file=output_file)
    info = Information(f"generation_mutation_prob=0.7.txt")
    info.read_file()
    info.plot_graph(f"Fitness/Generation for Mutation Probability = 0.7")


if __name__ == '__main__':
    main()

