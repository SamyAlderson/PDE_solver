# PDE_solver

A Python-based partial differential equation (PDE) solver using the finite difference method.

## Overview
PDE_solver is a numerical tool designed to solve a wide range of PDE problems, including elliptical, parabolic, and hyperbolic equations. By leveraging the finite difference method, this project aims to provide an efficient and accurate solution to complex problems in various fields, such as physics, engineering, and mathematics. This project is particularly useful for researchers and practitioners who need to simulate and analyze PDE-based systems.

## Features
- **Finite Difference Method**: A numerical method for solving PDEs using discrete approximations.
- **Grid Generation**: Automatic grid generation for efficient computation.
- **Boundary Conditions**: Support for various boundary conditions, including Dirichlet, Neumann, and Robin conditions.
- **Error Analysis**: Built-in error analysis for assessing the accuracy of the solution.
- **Visualization**: Interactive visualization tools for exploring the solution.
- **Parallel Computing**: Support for parallel computing using multiple threads or processes.
- **Easy Integration**: Easy integration with other libraries and frameworks.

## Getting Started

### Prerequisites
- Python 3.9+
- NumPy 1.20+
- SciPy 1.7+
- Matplotlib 3.4+

### Installation
```bash
# Install required packages
pip install -r requirements.txt

# Clone the repository
git clone https://github.com/username/PDE_solver.git

# Navigate to the project directory
cd PDE_solver

# Install the project dependencies
pip install .
```

### Usage
```bash
# Run the PDE solver
python src/main.py -i input_data.csv -o output_data.csv

# View the solution using Matplotlib
python src/visualisation.py -i output_data.csv
```

## Architecture
The project structure is organized into the following directories:

- `src`: Source code for the PDE solver and visualization tools.
- `tests`: Unit tests for the PDE solver and visualization tools.
- `docs`: Documentation for the project, including this README file.
- `requirements.txt`: List of required packages and dependencies.
- `input_data.csv`: Sample input data for the PDE solver.
- `output_data.csv`: Sample output data for the PDE solver.

## API Reference
The PDE solver uses the following public interfaces:

- `pde_solver.solve(grid, boundary_conditions, initial_conditions)`: Solve the PDE using the finite difference method.
- `grid.generate(nx, ny, dx, dy)`: Generate a regular grid with the specified dimensions and spacing.
- `boundary_conditions.apply(grid, boundary_values)`: Apply the specified boundary conditions to the grid.
- `initial_conditions.apply(grid, initial_values)`: Apply the specified initial conditions to the grid.

## Testing
```bash
# Run the unit tests
python -m unittest discover -s tests

# Run the integration tests
python -m unittest discover -s tests/integration
```

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push and open a PR

## License
MIT License