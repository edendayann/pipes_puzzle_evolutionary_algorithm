import random
from eckity.genetic_operators.genetic_operator import GeneticOperator


class MutateStrategy(GeneticOperator):
    def __init__(self, probability=1, arity=2, events=None):
        """
            Vector N Point Mutation.

            Randomly chooses N vector cells and performs a small change in their values.

            Parameters
            ----------
            probability : float
                The probability of the mutation operator to be applied

            arity : int
                The number of individuals this mutation is applied on

            events: list of strings
                Events to publish before/after the mutation operator
        """
        self.individuals = None
        self.applied_individuals = None
        self.points = None
        super().__init__(probability=probability, arity=arity, events=events)

    def apply(self, individuals):
        """
        Attempt to perform the mutation operator

        Parameters
        ----------
        individuals : list of individuals
            individuals to perform crossover on
            will only receive one individual.

        Returns
        ----------
        list of individuals
            individuals after the crossover
        """

        rand = random.uniform(0.0, 1.0)
        if rand <= self.cutoff:
            individuals[0].change_strategy_factor()

        self.applied_individuals = individuals
        return individuals
