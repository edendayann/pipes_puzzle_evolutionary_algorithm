from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator
from eckity.fitness.simple_fitness import SimpleFitness
from overrides import overrides

from BoardIndividual import BoardIndividual
from ShapesDFS import ShapesDFS


class BoardEvaluator(SimpleIndividualEvaluator):
    def __init__(self, size, board_shapes, optimal_solution, moves_range=4, is_moves=False):
        super().__init__()
        self.size = size
        self.board_shapes = board_shapes
        self.optimal_solution = optimal_solution
        self.optimal_moves = sum(self.optimal_solution)
        self.moves_range = moves_range
        self.is_moves = is_moves

    @overrides
    def evaluate_individual(self, individual):
        solution = individual.get_vector()
        fitness = 0
        if self.is_moves:
            moves = moves_calculation(solution)
            if moves - self.optimal_moves > 0:
                fitness = (self.optimal_moves - moves) / self.moves_range
        dfs = ShapesDFS(self.board_shapes, solution, self.size)
        dfs.DFS()
        fitness += dfs.max_group_size - 0.5 * dfs.out_of_bounds
        i = 0
        for shape in self.board_shapes:
            if shape != '/':
                if shape == 'l':  # l shape has only 2 different states
                    solution[i] = solution[i] % 2
                if solution[i] == self.optimal_solution[i]:
                    fitness += 1
                else:
                    fitness -= 1
                i += 1
        return fitness


def moves_calculation(solution):
    moves = 0
    for i in range(len(solution)):
        moves += solution[i]
        solution[i] = solution[i] % 4
    return moves


def eval_test():
    board_shapes = 'LTLi/iiTL/LTTi/iLli'
    solution = [43, 40, 2, 40, 2, 2, 1, 41, 3, 40, 2, 3, 42, 0, 43, 3]
    # solution = [3, 0, 2, 0, 2, 2, 1, 1, 3, 0, 2, 3, 2, 0, 1, 3]
    optimal_solution = [3, 0, 2, 0, 2, 2, 1, 1, 3, 0, 2, 3, 2, 0, 1, 3]
    board_eval = BoardEvaluator(4, board_shapes, optimal_solution, 50, True)
    individual = BoardIndividual(fitness=SimpleFitness(higher_is_better=True), size=4)
    individual.set_vector(solution)
    print(sum(solution))
    print(board_eval.evaluate_individual(individual))


if __name__ == '__main__':
    eval_test()
