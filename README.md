# Pacman AI – Search Algorithms

An Artificial Intelligence project based on the Berkeley CS188 Pacman environment, implementing classical search algorithms to solve maze navigation and pathfinding problems.

## 📌 Project Overview

The objective of this project is to understand and implement fundamental AI search techniques by navigating Pacman through different maze environments.

Pacman explores the maze to reach a goal while following different search strategies. Each algorithm determines how the search space is explored and how a solution is found.

## 🧠 Algorithms Implemented

The project includes the following search algorithms:

| Algorithm | Description |
|---|---|
| Depth-First Search (DFS) | Explores one branch deeply before backtracking. |
| Breadth-First Search (BFS) | Explores nodes level by level. |
| Uniform Cost Search (UCS) | Expands the node with the lowest cumulative path cost. |
| A* Search | Combines path cost and heuristic estimation to find an efficient path. |
| AO* Search | Uses heuristic-guided search on AND-OR graphs to find an optimal solution subgraph. |

## 🎮 Pacman Environment

The algorithms are explored and tested using different maze layouts, such as:

- Tiny Maze
- Medium Maze
- Large Maze

The project also explores heuristic-based search and AO* problem-solving through practical examples and dry runs.

## 🛠️ Technologies Used

- Python
- Artificial Intelligence
- Graph Search Algorithms
- Heuristic Search
- Berkeley Pacman Environment

## 🚀 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/pacman-ai-search-algorithms.git
   ```

2. Navigate to the project directory:

   ```bash
   cd pacman-ai-search-algorithms
   ```

3. Run Pacman using a search algorithm:

   ```bash
   python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
   ```

4. Try other algorithms:

   **DFS**
   ```bash
   python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
   ```

   **UCS**
   ```bash
   python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
   ```

   **A***
   ```bash
   python pacman.py -l mediumMaze -p SearchAgent -a fn=astar
   ```

*Note: These commands assume the standard Berkeley Pacman project structure and the corresponding search functions are implemented.*

## 🔍 AO* Algorithm

AO* (AND-OR Search) is a heuristic search algorithm used for problems that can be represented using AND-OR graphs.

- **OR nodes:** Any one child can provide a solution.
- **AND nodes:** All required children must be solved.
- Uses heuristic estimates to guide the search.
- Updates costs and revises the solution graph as better paths are discovered.

AO* was also explored through maze-based examples and manual dry runs.

## 📚 Learning Outcomes

Through this project, I explored:

- State-space representation and graph traversal.
- Frontier management using stacks, queues, and priority queues.
- Pathfinding and cost-based search.
- Heuristic functions and informed search.
- AND-OR graph representation and AO* search.
- Differences between uninformed and informed search strategies.
- Practical applications of AI in game environments.

## 👨‍💻 Author

**Sayan Halder**

Computer Science | Artificial Intelligence | Software Development

## 🙏 Acknowledgement

Based on the Berkeley CS188 Pacman AI educational project. Original framework and course materials belong to their respective creators.