from eckity.creators.creator import Creator
from eckity.fitness.simple_fitness import SimpleFitness

from BoardIndividual import BoardIndividual


class BoardCreator(Creator):
    def __init__(self,
                 events=None,
                 size=3):
        # if events is None:
        #     events = ["after_creation"]
        super().__init__(events)
        self.created_individuals = None
        self.type = BoardIndividual
        self.size = size
        # self.board_shapes = 'ILT/TLI/ITL'
        # self.board_solution = '123/123/123'

    def create_individuals(self, n_individuals, higher_is_better):
        individuals = [self.type(fitness=SimpleFitness(higher_is_better=higher_is_better),
                                 size=self.size) for i in range(n_individuals)]
        for indi in individuals:
            print(indi.show())
        self.created_individuals = individuals
        return individuals
