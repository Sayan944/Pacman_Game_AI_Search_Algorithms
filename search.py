# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    stack = util.Stack()

    start = problem.getStartState()
    stack.push((start, []))

    visited = set()

    while not stack.isEmpty():
        state, actions = stack.pop()

        if state in visited:
            continue

        visited.add(state)

        if problem.isGoalState(state):
            return actions

        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in visited:
                stack.push((successor, actions + [action]))

    return []
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    queue = util.Queue()

    start = problem.getStartState()
    queue.push((start, []))

    visited = set()

    while not queue.isEmpty():

        state, actions = queue.pop()

        if state in visited:
            continue

        visited.add(state)

        if problem.isGoalState(state):
            return actions

        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in visited:
                queue.push((successor, actions + [action]))

    return []
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    queue = util.PriorityQueue()

    start = problem.getStartState()
    queue.push((start, []), 0)

    visited = set()

    while not queue.isEmpty():

        state, actions = queue.pop()

        if state in visited:
            continue

        visited.add(state)

        if problem.isGoalState(state):
            return actions

        for successor, action, stepCost in problem.getSuccessors(state):

            if successor not in visited:

                cost = problem.getCostOfActions(actions + [action])

                queue.push((successor, actions + [action]), cost)

    return []
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    queue = util.PriorityQueue()

    start = problem.getStartState()
    queue.push((start, []), 0)

    visited = set()

    while not queue.isEmpty():

        state, actions = queue.pop()

        if state in visited:
            continue

        visited.add(state)

        if problem.isGoalState(state):
            return actions

        for successor, action, stepCost in problem.getSuccessors(state):

            if successor not in visited:

                newActions = actions + [action]

                cost = problem.getCostOfActions(newActions)
                priority = cost + heuristic(successor, problem)

                queue.push((successor, newActions), priority)

    return []
    util.raiseNotDefined()



def aoStarSearch(problem):
    """
    AO* search for the Pacman PositionSearchProblem.

    The Pacman maze is an OR graph:
    from each position, Pacman chooses one possible move.
    Therefore, AO* uses the minimum-cost successor at each state.

    The heuristic used here is Manhattan distance to the goal.
    """

    start = problem.getStartState()

    # Store estimated cost of each state
    h = {}

    # Store the best successor selected by AO*
    best = {}

    # States whose best solution has been completely solved
    solved = set()

    # Successors generated for each state
    expanded = {}

    # Edges that lead to a dead end/cycle
    blocked = set()

    # States currently being explored
    visiting = set()

    def heuristic(state):
        """
        Manhattan distance from current state to goal.
        """
        if hasattr(problem, 'goal'):
            return abs(state[0] - problem.goal[0]) + \
                   abs(state[1] - problem.goal[1])

        return 0

    def estimate(state):
        """
        Get the heuristic estimate of a state.
        """
        if state not in h:
            h[state] = heuristic(state)

        return h[state]

    def solve(state):
        """
        AO* recursively explores the most promising successor
        and propagates updated costs backward.
        """

        # Goal state
        if problem.isGoalState(state):
            h[state] = 0
            solved.add(state)
            return 0

        # Already solved
        if state in solved:
            return h[state]

        # Prevent infinite loops caused by maze cycles
        if state in visiting:
            return float('inf')

        visiting.add(state)

        # Expand the state only once
        if state not in expanded:
            expanded[state] = problem.getSuccessors(state)

        successors = expanded[state]

        # Dead end
        if len(successors) == 0:
            h[state] = float('inf')
            visiting.remove(state)
            return float('inf')

        while True:

            # Calculate the cost of every possible successor
            choices = []

            for successor, action, stepCost in successors:

                # Ignore a successor that has already been found
                # to create a dead end/cycle
                if (state, successor) in blocked:
                    continue

                value = stepCost + estimate(successor)

                choices.append(
                    (value, successor, action, stepCost)
                )

            # No usable successor
            if len(choices) == 0:
                h[state] = float('inf')
                visiting.remove(state)
                return float('inf')

            # AO* chooses the minimum-cost branch
            value, successor, action, stepCost = min(
                choices,
                key=lambda x: x[0]
            )

            # Update estimated cost of current state
            h[state] = value

            # Remember the best decision
            best[state] = (successor, action)

            # If the selected child is already solved,
            # current state is also solved.
            if successor in solved:
                solved.add(state)
                visiting.remove(state)
                return h[state]

            # Otherwise recursively solve the selected child
            childValue = solve(successor)

            # Child cannot lead to the goal
            if childValue == float('inf'):
                blocked.add((state, successor))
                continue

            # Child was updated/solved.
            # Recalculate the current state.
            if successor in solved:
                continue

        visiting.remove(state)

    # Run AO* from the starting state
    result = solve(start)

    if result == float('inf'):
        return []

    # Reconstruct the final path
    actions = []
    current = start
    visited = set()

    while not problem.isGoalState(current):

        # Safety against unexpected cycles
        if current in visited:
            return []

        visited.add(current)

        if current not in best:
            return []

        successor, action = best[current]

        actions.append(action)
        current = successor

    return actions


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
aostar = aoStarSearch
