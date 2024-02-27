from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator
from eckity.fitness.simple_fitness import SimpleFitness
from overrides import overrides

from BoardIndividual import BoardIndividual
from ShapesDFS import ShapesDFS


class BoardEvaluator(SimpleIndividualEvaluator):
    def __init__(self, size, board_shapes, optimal_solution):
        super().__init__()
        self.size = size
        self.board_shapes = board_shapes
        self.optimal_solution = optimal_solution

    @overrides
    def evaluate_individual(self, individual):
        # TODO make it better
        solution = individual.get_vector()
        dfs = ShapesDFS(self.board_shapes, solution, self.size)
        dfs.DFS()
        fitness = (self.size * self.size) / dfs.groups - 0.5 * dfs.out_of_bounds
        for i in range(len(solution)):
            if solution[i] == self.optimal_solution[i]:
                fitness += 1
            else:
                fitness -= 1
        return fitness


def eval_test():
    board_shapes = 'LTLi/iiTL/LTTi/iLli'
    optimal_solution = [3, 0, 2, 0, 2, 2, 1, 1, 3, 0, 2, 3, 2, 0, 1, 3]
    board_eval = BoardEvaluator(4, board_shapes, optimal_solution)
    individual = BoardIndividual(fitness=SimpleFitness(higher_is_better=False), size=4)
    individual.set_vector(optimal_solution)
    print(board_eval.evaluate_individual(individual))


eval_test()
