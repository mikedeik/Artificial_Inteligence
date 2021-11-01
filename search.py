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

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
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
    """
    "*** YOUR CODE HERE ***"
    #getting the start state of the problem
    node = problem.getStartState()
    #if start state is goal state returns empty list(no actions taken)
    if problem.isGoalState(node):
        return []
    #we will use stack for DFS
    s = util.Stack()
    #init empty visited list
    visited = []
    actions = []
    # inserting in our queue a tuple with first element being the current state node and
    # 2nd element the actions required to get to that node (empty list since it's start node)
    s.push((node,actions))
    #loop while the stack is not empty
    while not s.isEmpty() :
        # pop the first item in the stack
        curr, actions = s.pop()
        # check if node is visited
        if curr not in visited:
            # tag as visited
            visited.append(curr)
            # if our current node is our Goal state returns the actions used to get there
            if problem.isGoalState(curr):
                return actions
            # we expand the curr node and get all its successors, actions and cost(we don't need that for now) to get to next node from our current 
            for succ,action,cost in problem.expand(curr):
                # and for each we push the new items in the stack
                nextaction = actions + [action]
                s.push((succ,nextaction))



             
    


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
     #getting the start state of the problem
    node = problem.getStartState()
    #if start state is goal state returns empty list(no actions taken)
    if problem.isGoalState(node):
        return []
    #we will use a Queue for BFS
    q = util.Queue()
    #init empty visited list
    visited = set() #change this to set() is getting error "Unhashable type list for q4 "
    actions = []
    # inserting in our queue a tuple with first element being the current state node and
    # 2nd element the actions required to get to that node (empty list since it's start node)
    q.push((node,actions))
    #loop while the queue is not empty
    while not q.isEmpty() :
        # pop the first item in the queue here 
        curr, actions = q.pop()
        
        # if our current node is our Goal state returns the actions used to get there
        if problem.isGoalState(curr):
            return actions
        # check if node is visited
        if curr not in visited:
            # tag as visited
            visited.add(curr)
            
            # we expand the curr node and get all its successors, actions and cost(we don't need that for now) to get to next node from our current 
            for succ,action,cost in problem.expand(curr):
                # and for each we push the new items in the queue 
                nextaction = actions + [action]
                q.push((succ,nextaction))

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    state = problem.getStartState()
    if problem.isGoalState(state):
        return []
    PQ = util.PriorityQueue()
    visited = set()
    actions = []

    PQ.push((state, actions , 0), heuristic(state,problem))
    while not PQ.isEmpty():
        curr,actions,cost = PQ.pop()
        if problem.isGoalState(curr):
                return actions
        if curr not in visited:
            visited.add(curr)          
            for next,action,nextcost in problem.expand(curr):
                nextaction = actions + [action]
                newcost =  cost + nextcost
                finalcost = newcost + heuristic(next,problem)
                PQ.push((next,nextaction,newcost),finalcost) 


   # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
