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
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    # Note: every state is a tuple (coordinates of current state,traveled_path)

    path = []  # init path
    stack = util.Stack()  # init stack
    stack.push((problem.getStartState(), []))  # push first state to stack
    visited = []  # init vidited list
    while not stack.isEmpty():  # repeat until stack become empty
        node, path = stack.pop()  # pop from stack
        visited.append(node)  # add node to visited
        if problem.isGoalState(node):   # check if node is goal and break
            break
        else:  # node is not goal -> countinue
            succ = problem.getSuccessors(node)  # get node successors
            for n in succ:  # do following for all successors of node
                if not n[0] in visited:  # check if successor is not in visisted list
                    direction = [n[1]]  # get current direction
                    temp_path = path + direction  # add direction to path
                    # push new state and path to stack
                    stack.push((n[0], temp_path))
    return path  # return created path
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # Note: every state is a tuple (coordinates of current state,traveled_path)
    path = []  # init path
    queue = util.Queue()  # init queue
    queue.push((problem.getStartState(), []))  # push first state to queue
    # we add successors of expaded nod to expanded_succs
    expanded_succs = [problem.getStartState()]  # init list with start state
    while not queue.isEmpty():  # repeat until queue become empty
        node, path = queue.pop()  # pop from queue
        if problem.isGoalState(node):   # check if node is goal and break
            break
        else:  # node is not goal -> countinue
            succ = problem.getSuccessors(node)  # get node successors
            for n in succ:  # do following for all successors of node
                # check if successor is not in expanded_succs list
                if not n[0] in expanded_succs:
                    direction = [n[1]]  # get current direction
                    temp_path = path + direction  # add direction to path
                    # push new state and path to queue
                    queue.push((n[0], temp_path))
                    # add successors to expanded_succs
                    expanded_succs.append(n[0])
    return path  # return created path
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    # Note: every state is a tuple (coordinates of current state,traveled_path)

    path = []  # init path
    pq = util.PriorityQueue()  # init priority queue
    # push first state to priority queue
    pq.push((problem.getStartState(), []), 0)
    visisted = []  # init visited list
    while not pq.isEmpty():  # repeat until queue become empty
        node, path = pq.pop()  # pop from queue
        if node in visisted:  # check if node is in visited list and countinue
            continue
        else:  # otherwise do following
            visisted.append(node)
            if problem.isGoalState(node):   # check if node is goal and break
                break
            else:  # node is not goal -> countinue
                succ = problem.getSuccessors(node)  # get node's successors
                for n in succ:  # do following for all successors of node
                    direction = [n[1]]  # get current direction
                    temp_path = path + direction  # add direction to path
                    # push new state and path to priority queue
                    pq.update((n[0], temp_path),
                              problem.getCostOfActions(temp_path))

    return path  # return created path
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    # Note: every state is a tuple (coordinates of current state,traveled_path)

    path = []  # init path
    pq = util.PriorityQueue()  # init priority queue
    # push first state to priority queue
    pq.push((problem.getStartState(), []), 0 +
            heuristic(problem.getStartState(), problem))
    visisted = []  # init visited list
    while not pq.isEmpty():  # repeat until queue become empty
        node, path = pq.pop()  # pop from queue
        if node in visisted:  # check if node is in visited list and countinue
            continue
        else:  # otherwise do following
            visisted.append(node)
            if problem.isGoalState(node):   # check if node is goal and break
                break
            else:  # node is not goal -> countinue
                succ = problem.getSuccessors(node)  # get node's successors
                for n in succ:  # do following for all successors of node
                    direction = [n[1]]  # get current direction
                    temp_path = path + direction  # add direction to path
                    # push new state and path to priority queue
                    pq.update((n[0], temp_path),
                              problem.getCostOfActions(
                                  temp_path)+heuristic(n[0], problem))
    return path  # return created path
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
