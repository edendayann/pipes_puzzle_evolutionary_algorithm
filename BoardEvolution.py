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

    def evolve(self):
        """
        Performs the evolutionary run by initializing the random seed, creating the population,
        performing the evolutionary loop and finally finishing the evolution process
        """
        self.initialize()

        if self.termination_checker.should_terminate(self.population,
                                                     self.best_of_run_,
                                                     self.generation_num):
            self.final_generation_ = 0
            self.publish('after_generation')
        else:
            self.evolve_main_loop()

        self.publish('evolution_finished')
        return self.best_of_run_.get_vector(), self.best_of_run_.get_augmented_fitness()
