"""
Module de gestion du maillage.

Ce module contient la logique de gestion du maillage, qui est utilisé pour résoudre les problèmes aux dérivées partielles.
"""

import numpy as np
from typing import Tuple, List

class Grid:
    """
    Classe représentant le maillage.

    Le maillage est représenté par une grille de points dans l'espace.

    Attributes:
        nx (int): Nombre de points dans la direction x.
        ny (int): Nombre de points dans la direction y.
        x (numpy.ndarray): Coordonnées x des points du maillage.
        y (numpy.ndarray): Coordonnées y des points du maillage.
    """

    def __init__(self, nx: int, ny: int):
        """
        Crée un nouveau maillage.

        Args:
            nx (int): Nombre de points dans la direction x.
            ny (int): Nombre de points dans la direction y.
        """
        if nx <= 0 or ny <= 0:
            raise ValueError("Le nombre de points dans les directions x et y doit être supérieur à 0")

        self.nx = nx
        self.ny = ny
        self.x = np.linspace(0, 1, nx)
        self.y = np.linspace(0, 1, ny)

    def get_points(self) -> Tuple[numpy.ndarray, numpy.ndarray]:
        """
        Récupère les coordonnées des points du maillage.

        Returns:
            Tuple[numpy.ndarray, numpy.ndarray]: Coordonnées x et y des points du maillage.
        """
        return self.x, self.y

    def get_grid(self) -> numpy.ndarray:
        """
        Récupère la grille de points du maillage.

        Returns:
            numpy.ndarray: Grille de points du maillage.
        """
        return np.meshgrid(self.x, self.y)

class GridError(Exception):
    """
    Classe d'erreur pour les problèmes liés au maillage.
    """

class GridNotFoundError(GridError):
    """
    Classe d'erreur pour les problèmes liés à la recherche du maillage.
    """

class GridCreationError(GridError):
    """
    Classe d'erreur pour les problèmes liés à la création du maillage.
    """

def create_grid(nx: int, ny: int) -> Grid:
    """
    Crée un nouveau maillage.

    Args:
        nx (int): Nombre de points dans la direction x.
        ny (int): Nombre de points dans la direction y.

    Returns:
        Grid: Le maillage créé.
    """
    return Grid(nx, ny)