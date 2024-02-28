from eckity.creators.creator import Creator
from eckity.fitness.simple_fitness import SimpleFitness

from BoardIndividual import BoardIndividual


class BoardCreator(Creator):
    def __init__(self, events=None, size=3, moves_range=4):
        if events is None:
            events = ["after_creation"]
        super().__init__(events)
        self.created_individuals = None
        self.type = BoardIndividual
        self.size = size
        self.moves_range = moves_range

    def create_individuals(self, n_individuals, higher_is_better):
        individuals = [self.type(fitness=SimpleFitness(higher_is_better=higher_is_better), size=self.size,
                                 moves_range=self.moves_range) for i in range(n_individuals)]
        self.created_individuals = individuals
        return individuals
