from eckity.genetic_encodings.ga.vector_individual import Vector
from eckity.fitness.fitness import Fitness
import random


class BoardIndividual(Vector):
    counter = 1  # First population is irrelevant to the overall calculation.

    def __init__(self, fitness: Fitness, size=3, moves_range=4):
        super().__init__(fitness, bounds=(0, 3))
        self.row = size
        self.id = BoardIndividual.counter
        BoardIndividual.counter += 1
        self.moves_generator(moves_range)

    def get_augmented_fitness(self):
        return self.fitness.get_augmented_fitness(self)

    def show(self):
        print(f"id: {self.id}, size: {self.size()}")
        print(self.get_vector())

    def moves_generator(self, moves_range):
        solution = []
        for i in range(self.row):
            for j in range(self.row):
                solution.append(random.randrange(moves_range))
        self.set_vector(solution)

    def get_random_number_in_bounds(self, index):
        return random.randrange(4)
