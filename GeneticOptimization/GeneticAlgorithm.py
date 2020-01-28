import random

class GeneticAlgorithm:

    def __init__(self, opProblem, populationSize, beta, epsilon):
        """

        :param opProblem: the optimization problem object to solve
        :param beta: the parameter in the exponential distribution for the stochastic cross over events.
        # Will the the mean median choice of the next generation cross over (median of sorted characters in fitness)
        """
        self.problem = opProblem
        self.beta = beta
        self.populationSize = populationSize
        self.epsilon = epsilon

    def solve(self):
        """
        Return a single vector that the algorithm has converged on
        :return: vector coordinates
        """

        # Generate initial random population
        currPop = []
        nextPop = []

        while len(nextPop) == 0 or abs(currPop[0] - nextPop[0]) > self.epsilon:
            # Evalute their fitnesses
            fitnessCharacters = [(character, self.fitness2D(character)) for character in currPop]
            sorted(fitnessCharacters, key=lambda x:x[1])
            # Cross over generations until THE BEST individual in subsequent populations does not differ by epsilon
            nextPop = self.crossOver(fitnessCharacters)


    def fitness2D(self, character):
        """
        Evaluate the fitness of the given character
        :param character: a vector point
        :return:
        """

        return sum([(character[0] - p[0])**2 + (character[1] - p[1])**2 for p in self.problem.locations])


    def crossOver(self, lastfitness):
        """

        :param last:
        :return:
        """