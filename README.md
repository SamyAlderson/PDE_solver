# PDE_solver
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![CI](https://github.com/username/PDE_solver/actions/workflows/main.yml/badge.svg)

## Description

Le projet PDE_solver est une implémentation de résolveur de problèmes aux dérivées partielles (PDE) utilisant la méthode des différences finies. Il est conçu pour résoudre des problèmes de type elliptique, parabolique et hyperbolique.

## Fonctionnalités

- Résolution de problèmes PDE avec la méthode des différences finies
- Gestion du maillage pour la résolution des PDE
- Visualisation des résultats avec des graphiques 2D et 3D
- Fichier de test pour le résolveur de PDE et la gestion du maillage

## Installation

Pour installer le projet, vous devez avoir Python 3.9 ou supérieur installé sur votre ordinateur. Vous pouvez installer les dépendances nécessaires en exécutant la commande suivante dans le répertoire du projet :
```bash
pip install -r requirements.txt
```
## Usage

Pour utiliser le projet, vous devez exécuter le fichier `main.py` avec l'option `-h` pour afficher les options disponibles :
```bash
python src/main.py -h
```
Voici un exemple de commande pour résoudre un problème PDE :
```bash
python src/main.py -i example/input.txt -o example/output.txt
```
## Architecture du projet

Le projet est organisé en plusieurs fichiers :

- `src/main.py` : Fichier principal qui gère l'exécution du projet
- `src/pde_solver.py` : Fichier contenant la logique de résolution du PDE
- `src/grid.py` : Fichier contenant la logique de gestion du maillage
- `src/visualisation.py` : Fichier contenant la logique de visualisation des résultats
- `tests/test_pde_solver.py` : Fichier de test pour le résolveur de PDE
- `tests/test_grid.py` : Fichier de test pour la gestion du maillage

## Contribuer

Pour contribuer au projet, vous pouvez suivre les étapes suivantes :

1. Créez un compte sur GitHub et vous abonnez au projet.
2. Clonez le projet sur votre ordinateur avec la commande suivante :
```bash
git clone https://github.com/username/PDE_solver.git
```
3. Créez une branche pour votre contribution avec la commande suivante :
```bash
git checkout -b nom-de-la-branche
```
4. Modifiez les fichiers du projet pour ajouter votre contribution.
5. Validez vos modifications avec la commande suivante :
```bash
git add .
git commit -m "Message de validation"
```
6. Envoyez une demande de pull request pour que les autres développeurs puissent vous aider à valider vos modifications.

## Licence

Le projet PDE_solver est sous licence MIT. Vous pouvez l'utiliser et la partager librement, mais vous devez inclure la mention de la licence dans vos travaux dérivés.