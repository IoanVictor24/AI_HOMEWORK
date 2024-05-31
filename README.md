# Traveling Salesman Problem Solver

This Python project aims to tackle the classic Traveling Salesman Problem (TSP) using various search algorithms, including Breadth-First Search (BFS), Uniform Cost Search (UCS), and A* Search.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/tsp-solver.git
    cd tsp-solver
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Prepare the input data**:
   - Create a distance matrix representing distances between cities.

2. **Run the solver**:
    ```bash
    python main.py
    ```

3. **View the results**:
   - The script outputs the optimal path and the minimum maximum distance.

## Example

Example distance matrix:
```python
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
