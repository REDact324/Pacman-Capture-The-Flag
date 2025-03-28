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

def depthFirstSearch(problem):
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
    _visited = {}
    node = problem.getStartState()
    _visited[node] = True
    for item in problem.getSuccessors(node):
        stack.push((item, [item[1]]))

    while not stack.isEmpty():
        node, path = stack.pop()

        if node[0] not in _visited:
            _visited[node[0]] = True
        else:
            continue

        if problem.isGoalState(node[0]):
            return path

        for item in problem.getSuccessors(node[0]):
            if item[0] not in _visited:
                stack.push((item, path + [item[1]]))

    return []

    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    queue = util.Queue()
    _visited = {}
    node = problem.getStartState()
    _visited[node] = True
    for item in problem.getSuccessors(node):
        queue.push((item, [item[1]]))

    while not queue.isEmpty():
        node, path = queue.pop()

        if node[0] not in _visited:
            _visited[node[0]] = True
        else:
            continue

        if problem.isGoalState(node[0]):
            return path

        for item in problem.getSuccessors(node[0]):
            if item[0] not in _visited:
                queue.push((item, path + [item[1]]))

    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    pq = util.PriorityQueue()
    _visited = {}
    node = problem.getStartState()
    _visited[node] = True
    for item in problem.getSuccessors(node):
        pq.push((item, [item[1]], item[2]), item[2])

    while not pq.isEmpty():
        node, path, cost = pq.pop()

        if node[0] not in _visited:
            _visited[node[0]] = True
        else:
            continue

        if problem.isGoalState(node[0]):
            return path

        for item in problem.getSuccessors(node[0]):
            if item[0] not in _visited:
                pq.update((item, path + [item[1]], cost + item[2]), cost + item[2])

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    pq = util.PriorityQueue()
    _visited = {}
    node = problem.getStartState()
    _visited[node] = True
    for item in problem.getSuccessors(node):
        cost = item[2] + heuristic(item[0], problem)
        pq.push((item, [item[1]], cost), cost)

    while not pq.isEmpty():
        node, path, cost = pq.pop()

        if node[0] not in _visited:
            _visited[node[0]] = True
        else:
            continue

        if problem.isGoalState(node[0]):
            return path

        for item in problem.getSuccessors(node[0]):
            if item[0] not in _visited:
                new_cost = cost - heuristic(node[0], problem) + item[2] + heuristic(item[0], problem)
                pq.update((item, path + [item[1]], new_cost), new_cost)

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
