import sys
import logging
import time

from eckity.genetic_operators.crossovers.vector_k_point_crossover import VectorKPointsCrossover
from eckity.genetic_operators.mutations.vector_n_point_mutation import VectorNPointMutation
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.termination_checkers.threshold_from_target_termination_checker import ThresholdFromTargetTerminationChecker

from BoardCreator import BoardCreator
from BoardEvaluator import BoardEvaluator
from BoardEvolution import BoardEvolution
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation


def mut_val_getter(vec, idx):
    return vec.get_random_number_in_bounds(idx)


def main():
    # start = time.time()

    # n = len(sys.argv)
    # if  1 < n < 8: # There is a FEN representation given in argv
    #     alg_is_white = sys.argv[2] == 'w'
    #     FEN = (' '.join(sys.argv[1:]))
    #
    # logging.error(f"FEN inserted is: {FEN}\n\n")
    size = 4
    board_shapes = 'LTLi/iiTL/LTTi/iLli'
    optimal_solution = [3, 0, 2, 0, 2, 2, 1, 1, 3, 0, 2, 3, 2, 0, 1, 3]
    # Initialize the evolutionary algorithm
    algo = BoardEvolution(
        Subpopulation(creators=BoardCreator(size=size),
                      population_size=100,
                      # user-defined fitness evaluation method
                      evaluator=BoardEvaluator(size=size, board_shapes=board_shapes, optimal_solution=optimal_solution),
                      # maximization problem (fitness is sum of values), so higher fitness is better
                      higher_is_better=True,
                      elitism_rate=0.05,
                      # genetic operators sequence to be applied in each generation
                      operators_sequence=[
                          VectorKPointsCrossover(probability=0.9, arity=2, k=1),
                          VectorNPointMutation(probability=0.2, arity=1, mut_val_getter=mut_val_getter)
                      ],
                      selection_methods=[  # TODO check if we want better
                          # (selection method, selection probability) tuple
                          (TournamentSelection(tournament_size=4, higher_is_better=False), 1)
                      ]
                      ),
        max_workers=4,
        max_generation=30,
        # TODO check if we want better
        termination_checker=ThresholdFromTargetTerminationChecker(optimal=0, threshold=0.001),
        statistics=BestAverageWorstStatistics()
    )

    algo.evolve()


# print(f"Evolutionary algorithm done in {int(time.time() - start)} seconds.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
