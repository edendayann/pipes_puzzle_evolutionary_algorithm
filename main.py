import time
import tkinter as tk
import os
import shutil

from eckity.fitness.simple_fitness import SimpleFitness
from eckity.genetic_operators.crossovers.vector_k_point_crossover import VectorKPointsCrossover
from eckity.genetic_operators.mutations.vector_n_point_mutation import VectorNPointMutation
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.termination_checkers.threshold_from_target_termination_checker import ThresholdFromTargetTerminationChecker
from BoardCreator import BoardCreator
from BoardEvaluator import BoardEvaluator
from BoardEvolution import BoardEvolution
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation
from BoardIndividual import BoardIndividual
from UI import PipesPuzzleUI


def start_algorithm(board_size, is_moves, population_size, elitism_rate, max_generation, output_file, moves_range=4,
                    crossover_prob=0.9, mutation_prob=0.5):
    start = time.time()

    # Initialize the evolutionary algorithm
    algo = BoardEvolution(
        Subpopulation(creators=BoardCreator(size=board_size, moves_range=moves_range),
                      population_size=population_size,
                      # user-defined fitness evaluation method
                      evaluator=BoardEvaluator(size=board_size, is_moves=is_moves,
                                               moves_range=moves_range),
                      # maximization problem (fitness is sum of values), so higher fitness is better
                      higher_is_better=True,
                      elitism_rate=elitism_rate,
                      # genetic operators sequence to be applied in each generation
                      operators_sequence=[
                          VectorKPointsCrossover(probability=crossover_prob, arity=2, k=1),
                          VectorNPointMutation(probability=mutation_prob, arity=1, mut_val_getter=mut_val_getter)
                      ],
                      selection_methods=[
                          # (selection method, selection probability) tuple
                          (TournamentSelection(tournament_size=4, higher_is_better=True), 1)
                      ]
                      ),
        max_workers=4,
        max_generation=max_generation,
        termination_checker=ThresholdFromTargetTerminationChecker(optimal=10.0, threshold=0.001, higher_is_better=True),
        statistics=BestAverageWorstStatistics(output_stream=output_file)
    )

    best_sol, best_score = algo.evolve()
    return best_sol, best_score, int(time.time() - start)


def eval_solution(size, board_shapes, solution):
    board_eval = BoardEvaluator(size, board_shapes, solution)
    individual = BoardIndividual(fitness=SimpleFitness(higher_is_better=False), size=size)
    individual.set_vector(solution)
    return board_eval.evaluate_individual(individual)


def mut_val_getter(vec, idx):
    return vec.get_random_number_in_bounds(idx)


def main():
    clear_folder("output")
    root = tk.Tk()
    PipesPuzzleUI(root, start_algorithm)
    root.mainloop()


def clear_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
