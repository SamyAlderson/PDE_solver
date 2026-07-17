"""
Projet: PDE_solver
Description: Résolveur de problèmes aux dérivées partielles utilisant la méthode des différences finies
Langage: python
"""

import logging
import argparse
from src.pde_solver import PDE_solver
from src.grid import Grid
from src.visualisation import Visualisation

def main():
    """
    Fichier principal du projet.
    """
    # Configuration de la logger
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Récupération des argument de ligne de commande
    parser = argparse.ArgumentParser(description="PDE_solver")
    parser.add_argument("-f", "--file", help="Fichier de configuration", required=True)
    parser.add_argument("-o", "--output", help="Fichier de sortie", required=True)
    args = parser.parse_args()

    try:
        # Initialisation de la grille
        grid = Grid(args.file)

        # Initialisation du résolveur de PDE
        pde_solver = PDE_solver(grid)

        # Résolution du PDE
        logger.info("Résolution du PDE...")
        solution = pde_solver.solve()

        # Visualisation des résultats
        visualisation = Visualisation(solution)
        visualisation.plot(args.output)

        # Envoi de l'output
        logger.info("Envoi de l'output...")
        visualisation.save(args.output)

    except Exception as e:
        logger.error(f"Erreur: {str(e)}")
        raise

if __name__ == "__main__":
    main()