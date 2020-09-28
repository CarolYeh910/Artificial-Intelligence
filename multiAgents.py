# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """
    """
      coding by zsy
    """
    """
    def max_search(self,gameState,depth):
      if depth == self.depth or gameState.isWin() or gameState.isLose():
        return self.evaluationFunction(gameState)
      actions = gameState.getLegalActions(0)
      v = float('-Inf')
      for each in actions:
        successor = gameState.generateSuccessor(0,each)
        tempv = min_search(self,gameState,1,depth+1)
        if tempv > v:
          v = tempv
      return v
      coding by zsy
    def min_search(self,gameState,num,depth):
      if depth == self.depth or gameState.isWin() or gameState.isLose():
        return self.evaluationFunction(gameState)
      v = float('Inf')
      actions = gameState.getLegalActions(0)
      if num == gameState.getNumAgents() - 1:
        for each in actions:
          successor = gameState.generateSuccessor(num,each)
          tempv = max_search(self,gameState,num+1,depth+1)
          if tempv < v:
            v = tempv
        return v
      for each in actions:
          successor = gameState.generateSuccessor(num,each)
          tempv = min_search(self,gameState,num+1,depth+1)
          if tempv < v:
            v = tempv
      return v
      coding by zsy
      """


    def getAction(self, gameState):
      """
        coding by zsy
      """
      def max_search(state,depth):
        if depth == self.depth or state.isWin() or state.isLose():
          return self.evaluationFunction(state)
        #actions = State.getLegalActions(0)
        v = float('-Inf')
        for each in state.getLegalActions(0):
          #successor = State.generateSuccessor(0,each)
          tempv = min_search(state.generateSuccessor(0,each),1,depth)
          if tempv > v:
            v = tempv
        return v
      """
        coding by zsy
      """
      def min_search(state,num,depth):
        if state.isWin() or state.isLose():
          return self.evaluationFunction(state)
        v = float('Inf')
        #actions = State.getLegalActions(num)
        if num == state.getNumAgents() - 1:
          for each in state.getLegalActions(num):
            #successor = State.generateSuccessor(num,each)
            tempv = max_search(state.generateSuccessor(num,each),depth+1)
            if tempv < v:
              v = tempv
        else:
          for each in state.getLegalActions(num):
            #successor = State.generateSuccessor(num,each)
            tempv = min_search(state.generateSuccessor(num,each),num+1,depth)
            if tempv < v:
              v = tempv
        return v

      count = 0
      v = float('-Inf')
      if gameState.isWin() or gameState.isLose() or self.depth == 0:
        return None
      bestaction = ''
      for each in gameState.getLegalActions(0):
        tempv = min_search(gameState.generateSuccessor(0,each),1,0)
        if tempv > v:
          v = tempv
          bestaction = each
      return bestaction
      util.raiseNotDefined()
      """
          Returns the minimax action from the '''current gameState''' using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
          state.iswin()
      """
      """
          coding by zsy
      """
      """
        actions = gameState.getLegalActions(0)
        v = float('-Inf')
        best_action = actions[0]
        for each in actions:
          #successor = gameState.generateSuccessor(0,each)
          tempv = min_search(gameState.generateSuccessor(0,each),1,0)
          if tempv > v:
            v = tempv
            actions = each
        return actions
      """
      """
          coding by zsy
      """

      "*** YOUR CODE HERE ***"

      util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
      """
        coding by zsy
      """
      def max_search(state,depth,b):
        if depth == self.depth or state.isWin() or state.isLose():
          return self.evaluationFunction(state)
        #actions = State.getLegalActions(0)
        v = float('-Inf')
        a = float('-Inf')
        for each in state.getLegalActions(0):
          #successor = State.generateSuccessor(0,each)
          tempv = min_search(state.generateSuccessor(0,each),1,depth,a)
          if tempv > v:
            v = tempv
          if v >= b:
            return v
          a = max(a,v)
        return v
      """
        coding by zsy
      """
      def min_search(state,num,depth,a):
        if state.isWin() or state.isLose():
          return self.evaluationFunction(state)
        v = float('Inf')
        b = float('Inf')
        #actions = State.getLegalActions(num)
        if num == state.getNumAgents() - 1:
          for each in state.getLegalActions(num):
            #successor = State.generateSuccessor(num,each)
            tempv = max_search(state.generateSuccessor(num,each),depth+1,b)
            if tempv < v:
              v = tempv
            if v < a:
              return v
            b = min(b, v)
        else:
          for each in state.getLegalActions(num):
            #successor = State.generateSuccessor(num,each)
            tempv = min_search(state.generateSuccessor(num,each),num+1,depth,a) #your v is less than the a(a has found),return
            if tempv < v:
              v = tempv
            if v < a:
              return v
            b = min(b, v)
        return v

      count = 0
      v = float('-Inf')
      a = float('-Inf')
      if gameState.isWin() or gameState.isLose() or self.depth == 0:
        return None
      bestaction = ''
      for each in gameState.getLegalActions(0):
        tempv = min_search(gameState.generateSuccessor(0,each),1,0,a)
        if tempv > v:
          v = tempv
          bestaction = each
        a = max(a,v)
      return bestaction
      "*** YOUR CODE HERE ***"
      util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

