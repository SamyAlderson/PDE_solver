"""
Module de visualisation des résultats du résolveur de PDE.

Ce module utilise les bibliothèques matplotlib et numpy pour afficher les solutions de PDE
dans différentes formes (2D, 3D, etc.).
"""

import numpy as np
import matplotlib.pyplot as plt
from src.grid import Grid

class Visualisation:
    """
    Classe de visualisation des résultats du résolveur de PDE.

    Cette classe fournit des méthodes pour afficher les solutions de PDE dans différentes
    formes (2D, 3D, etc.).
    """

    def __init__(self, grid: Grid):
        """
        Initialise la classe Visualisation avec un maillage.

        :param grid: Le maillage du résolveur de PDE.
        """
        self.grid = grid

    def afficher_solution_2d(self, solution: np.ndarray):
        """
        Affiche la solution de PDE en 2D.

        :param solution: La solution de PDE en 2D.
        """
        plt.imshow(solution, cmap='hot', interpolation='nearest')
        plt.show()

    def afficher_solution_3d(self, solution: np.ndarray):
        """
        Affiche la solution de PDE en 3D.

        :param solution: La solution de PDE en 3D.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(solution, cmap='hot', edgecolor='none')
        plt.show()

    def afficher_solution_surface(self, solution: np.ndarray):
        """
        Affiche la solution de PDE comme surface.

        :param solution: La solution de PDE en 2D.
        """
        plt.imshow(solution, cmap='hot', interpolation='nearest')
        plt.show()

def main():
    """
    Fonction principale pour afficher les solutions de PDE.
    """
    grid = Grid()  # Crée un maillage
    visualisation = Visualisation(grid)  # Crée une instance de Visualisation

    # Récupère la solution de PDE
    solution = grid.resoudre_pde()  # Résout le PDE

    # Affiche la solution en 2D
    visualisation.afficher_solution_2d(solution)

    # Affiche la solution en 3D
    visualisation.afficher_solution_3d(solution)

    # Affiche la solution comme surface
    visualisation.afficher_solution_surface(solution)

if __name__ == "__main__":
    main()