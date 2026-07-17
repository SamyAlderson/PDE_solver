import unittest
import numpy as np
from pde_solver import PDE_solver

class TestPDE_solver(unittest.TestCase):
    def setUp(self):
        self.pde_solver = PDE_solver()

    def test_init(self):
        """
        Test si l'objet PDE_solver est créé avec succès.
        """
        self.assertIsInstance(self.pde_solver, PDE_solver)

    def test_solve_pde(self):
        """
        Test si la méthode solve_pde résout correctement un PDE linéaire.
        """
        # Définition du PDE linéaire à résoudre
        def pde(x, y):
            return np.sin(x) * np.cos(y)

        # Définition des conditions de bord
        def bc(x):
            return np.sin(x)

        # Résolution du PDE
        solution = self.pde_solver.solve_pde(pde, bc, (0, 1), (0, 1), 100, 100)

        # Vérification de la solution
        self.assertIsInstance(solution, np.ndarray)
        self.assertEqual(solution.shape, (100, 100))

    def test_solve_pde_invalid_input(self):
        """
        Test si la méthode solve_pde renvoie une erreur en cas d'input invalide.
        """
        with self.assertRaises(TypeError):
            self.pde_solver.solve_pde("invalid_input", lambda x: np.sin(x), (0, 1), (0, 1), 100, 100)

    def test_solve_pde_invalid_pde(self):
        """
        Test si la méthode solve_pde renvoie une erreur en cas de PDE invalid.
        """
        with self.assertRaises(ValueError):
            self.pde_solver.solve_pde(lambda x, y: np.sin(x) * np.cos(y) + 1, lambda x: np.sin(x), (0, 1), (0, 1), 100, 100)

if __name__ == '__main__':
    unittest.main()