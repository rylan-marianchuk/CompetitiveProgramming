import random
import plotly
class OptimizationProblem:
    def __init__(self, n_locations, n_lines, n_circles, range, is2d=True):
        """

        :param n_locations: the number of given locations to optimize distance with
        :param n_lines:
        :param n_circles:
        :param range: a single integer representing the border of problem area, max coordinate for locations
        :param is2d:
        """

        # List of vectors holding the desires locations  can be 2D or 3D
        self.locations = []

        if is2d:
            map(lambda x: self.locations.append(x), [(random.random()*range, random.random()*range) for _ in range(n_locations)])



    def plotScene(self):
        """
        Plot the unsolved scene for the optimization problem
        :return:
        """
        return