from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator
from overrides import overrides


class BoardEvaluator(SimpleIndividualEvaluator):
    def __init__(self, size, board_shapes, optimal_solution):
        super().__init__()
        self.size = size
        self.board_shapes = board_shapes
        self.optimal_solution = optimal_solution

    @overrides
    def evaluate_individual(self, individual):
        # TODO make it better
        fitness = 0
        solution = individual.get_vector()
        for i in range(len(solution)):
            if solution[i] == self.optimal_solution[i]:
                fitness += 1
            else:
                fitness -= 1
        return fitness

