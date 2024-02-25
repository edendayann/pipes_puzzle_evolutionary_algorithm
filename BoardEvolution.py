from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.evaluators.simple_population_evaluator import SimplePopulationEvaluator
from time import time
from overrides import overrides
import threading


class BoardEvolution(SimpleEvolution):
    """his class will work similarly to SimpleEvolution, will also support the integration of Communicator
       - a class that handles communication between the program and a number of chess engines """

    def __init__(self,
                 population,
                 max_workers,
                 max_generation,
                 termination_checker,
                 statistics):

        super().__init__(population, statistics=statistics, max_generation=max_generation,
                         termination_checker=termination_checker, max_workers=max_workers)

        # self.communicator = communicator

    # @overrides
    # def generation_iteration(self, gen):
    #     """
    #     Performs one iteration of the evolutionary run, for the current generation
    #
    #     Parameters
    #     ----------
    #     gen:
    #         current generation number (for example, generation #100)
    #
    #     Returns
    #     -------
    #     None.
    #     """
    #
    #     # breed population
    #     self.breeder.breed(self.population)
    #
    #     # Special sequence for BoardEvolution
    #     caller = threading.Event()
    #     self.communicator.initialize_movements_done(caller)
    #     # logging.error(f"==================== Generation in iteration no. {gen} ====================")
    #     for subpop in self.population.sub_populations:
    #         for ind in subpop.individuals:
    #             self.communicator.send_move_request(ind, self.executor)
    #
    #     caller.wait()  # waiting for all boards to be played
    #
    #     # Continue mostly like SimpleEvolution, only that best_of_gen isn't relevant.
    #     # Evaluate the entire population and get the best individual
    #     self.best_of_gen = self.population_evaluator.act(self.population)
    #
    #     self.best_of_run_ = self.best_of_gen  # We only care about the best_of_run
    #
    #     self.best_of_run_evaluator = self.population.sub_populations[0].evaluator
    #
    #     self.worst_of_gen = self.population.sub_populations[0].get_worst_individual()
