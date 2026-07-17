"""
Fichier de test pour la gestion du maillage
"""
import unittest
from src.grid import Grid, GridException
import numpy as np

class TestGrid(unittest.TestCase):
    def test_grid_creation(self):
        """
        Test de la création d'un maillage
        """
        grid = Grid(10, 10)
        self.assertIsNotNone(grid)
        self.assertEqual(grid.nb_x, 10)
        self.assertEqual(grid.nb_y, 10)

    def test_grid_creation_with_invalid_size(self):
        """
        Test de la création d'un maillage avec une taille invalid
        """
        with self.assertRaises(GridException):
            Grid(-1, 10)

    def test_grid_get_cell(self):
        """
        Test de la récupération d'une cellule du maillage
        """
        grid = Grid(10, 10)
        cell = grid.get_cell(5, 5)
        self.assertIsNotNone(cell)
        self.assertEqual(cell.x, 5)
        self.assertEqual(cell.y, 5)

    def test_grid_get_cell_out_of_bounds(self):
        """
        Test de la récupération d'une cellule hors des limites du maillage
        """
        grid = Grid(10, 10)
        with self.assertRaises(GridException):
            grid.get_cell(15, 15)

    def test_grid_neighborhood(self):
        """
        Test de la récupération des cellules voisines d'une cellule
        """
        grid = Grid(5, 5)
        cell = grid.get_cell(2, 2)
        neighborhood = cell.get_neighborhood(grid)
        self.assertEqual(len(neighborhood), 8)

    def test_grid_cell_properties(self):
        """
        Test de la récupération des propriétés d'une cellule
        """
        grid = Grid(10, 10)
        cell = grid.get_cell(5, 5)
        self.assertIsNotNone(cell.x)
        self.assertIsNotNone(cell.y)

class TestCell(unittest.TestCase):
    def test_cell_creation(self):
        """
        Test de la création d'une cellule
        """
        cell = Grid.Cell(5, 5)
        self.assertIsNotNone(cell)
        self.assertEqual(cell.x, 5)
        self.assertEqual(cell.y, 5)

    def test_cell_properties(self):
        """
        Test de la récupération des propriétés d'une cellule
        """
        cell = Grid.Cell(5, 5)
        self.assertIsNotNone(cell.x)
        self.assertIsNotNone(cell.y)

class TestGridException(unittest.TestCase):
    def test_grid_exception_creation(self):
        """
        Test de la création d'une exception Grid
        """
        exception = GridException("Erreur de maillage")
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Erreur de maillage")

if __name__ == '__main__':
    unittest.main()