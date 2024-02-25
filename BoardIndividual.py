from eckity.genetic_encodings.ga.vector_individual import Vector
from eckity.individual import Individual
from eckity.fitness.fitness import Fitness
# from MovementCalculation import MovementCalculation, MovementFactor

import random


class BoardIndividual(Vector):
    counter = 1  # First population is irrelevant to the overall calculation.

    # list_of_mov_fact = [MovementFactor.RightDefence, MovementFactor.LeftDefence, MovementFactor.RightAttack, MovementFactor.LeftAttack]
    def __init__(self, fitness: Fitness, size=3):
        super().__init__(fitness, bounds=(0, 3))
        self.row = size
        self.id = BoardIndividual.counter
        BoardIndividual.counter += 1
        # TODO check if happening good!
        self.states_generator()

    # def update_id(self):
    #     self.id = BoardIndividual.counter
    #     BoardIndividual.counter = (BoardIndividual.counter + 1) % 200

    def get_augmented_fitness(self):
        return self.fitness.get_augmented_fitness(self)

    def show(self):
        print(f"id: {self.id}, size: {self.size()}")
        print(self.get_vector())

    def states_generator(self):
        solution = []
        for i in range(self.row):
            for j in range(self.row):
                solution.append(random.randrange(4))
        self.set_vector(solution)

    def get_random_number_in_bounds(self, index):
        return random.randrange(4)
