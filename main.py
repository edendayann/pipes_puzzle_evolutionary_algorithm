import time

from eckity.fitness.simple_fitness import SimpleFitness
from eckity.genetic_operators.crossovers.vector_k_point_crossover import VectorKPointsCrossover
from eckity.genetic_operators.mutations.vector_n_point_mutation import VectorNPointMutation
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.termination_checkers.threshold_from_target_termination_checker import ThresholdFromTargetTerminationChecker

from BoardCreator import BoardCreator
from BoardEvaluator import BoardEvaluator
from BoardEvolution import BoardEvolution
from Boards import Boards
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation

from BoardIndividual import BoardIndividual





def main():
    start = time.time()

    size = int(input("Choose board size- 4/5/7: "))
    board = Boards(size)
    moves = input("Do you want to test moves- Y/N? ")
    if moves == 'Y' or moves == 'y':
        is_moves = True
        moves_range = int(input("How many? "))
    else:
        is_moves = False
        moves_range = 4
    population_size = int(input("Enter population size: "))
    elitism_rate = float(input("Enter elitism rate: "))
    # Initialize the evolutionary algorithm
    algo = BoardEvolution(
        Subpopulation(creators=BoardCreator(size=size, moves_range=moves_range),
                      population_size=population_size,
                      # user-defined fitness evaluation method
                      evaluator=BoardEvaluator(size=size, board_shapes=board.shapes,
                                               optimal_solution=board.optimal, is_moves=is_moves,
                                               moves_range=moves_range),
                      # maximization problem (fitness is sum of values), so higher fitness is better
                      higher_is_better=True,
                      elitism_rate=elitism_rate,
                      # genetic operators sequence to be applied in each generation
                      operators_sequence=[
                          VectorKPointsCrossover(probability=0.9, arity=2, k=1),
                          VectorNPointMutation(probability=0.2, arity=1, mut_val_getter=mut_val_getter)
                      ],
                      selection_methods=[  # TODO check if we want better
                          # (selection method, selection probability) tuple
                          (TournamentSelection(tournament_size=4, higher_is_better=True), 1)
                      ]
                      ),
        max_workers=4,
        max_generation=50,
        termination_checker=ThresholdFromTargetTerminationChecker(optimal=eval_optimal(size, board.shapes,
                                                                                       board.optimal),
                                                                  threshold=0.001, higher_is_better=True),
        statistics=BestAverageWorstStatistics()
    )

    algo.evolve()
    print(f"Evolutionary algorithm done in {int(time.time() - start)} seconds.")


def eval_optimal(size, board_shapes, optimal_solution):
    board_eval = BoardEvaluator(size, board_shapes, optimal_solution)
    individual = BoardIndividual(fitness=SimpleFitness(higher_is_better=False), size=size)
    individual.set_vector(optimal_solution)
    return board_eval.evaluate_individual(individual)


def mut_val_getter(vec, idx):
    return vec.get_random_number_in_bounds(idx)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
