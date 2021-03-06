# -*- coding: utf-8 -*-
# qlearningAgents.py
# ------------------
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


from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math

class QLearningAgent(ReinforcementAgent):
    """
      Q-Learning Agent

      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """
    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)
        
        # Al principi havia utilitzat un diccionari per emmagatzemar els QValues
        # pero al final em vaig adonar que hi havia una clase Counter a util que
        # resultava molt millor. (El codi comentat es la implementacio antiga i
        # es pot ignorar)
        
        # self.Q = {}
        
        self.Q = util.Counter()
        "*** YOUR CODE HERE ***"

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        "*** YOUR CODE HERE ***"
        """
        if state not in self.Q.keys():
            self.Q[state] = {}
            self.Q[state][action] = 0.0
        else:
            if action not in self.Q[state].keys():
                self.Q[state][action] = 0.0
        return self.Q[state][action]
        """
        return self.Q[state, action]
                


    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        "*** YOUR CODE HERE ***"
        """
        legalActions = self.getLegalActions(state)
        if len(legalActions)==0:
            return 0.0
        val = float('-inf')
        for action in legalActions:
            if self.getQValue(state,action) > val:
                val = self.getQValue(state,action)
        return val
        """
        values = [self.getQValue(state, action) for action in self.getLegalActions(state)]
        if len(values)!=0:
            return max(values)
        else:
            return 0.0

    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        "*** YOUR CODE HERE ***"
        """
        legalActions = self.getLegalActions(state)
        if len(legalActions)==0 or legalActions[0]=='exit':
            return 'exit'
        eqActions = []
        maxQ = float('-inf')
        for action in legalActions:
            if self.getQValue(state,action) > maxQ:
                maxQ = self.getQValue(state,action)
        
        for action in legalActions:
            if self.getQValue(state,action) == maxQ:
                eqActions.append(action)
        if len(eqActions) == 1:
            return eqActions[0]
        else:
            return random.choice(eqActions)
        """
        legalActions = self.getLegalActions(state)
        
        value = self.getValue(state)
        for action in legalActions:
            if (value == self.getQValue(state, action)):
                return action

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.

          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        # Pick Action
        legalActions = self.getLegalActions(state)
        action = None
        "*** YOUR CODE HERE ***"
        if len(legalActions)==0:
            return action
        if util.flipCoin(self.epsilon):
            return random.choice(legalActions)
        
        return self.getPolicy(state)

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here

          NOTE: You should never call this function,
          it will be called on your behalf
        """
        "*** YOUR CODE HERE ***"
        """
        maxQ = float('-inf')
        actions = self.getLegalActions(nextState)
        if len(actions)!=0:   
            for a in actions:
                if self.getQValue(nextState,a) > maxQ:
                    maxQ = self.getQValue(nextState,a)
        else:
            maxQ = 0.0
        if state not in self.Q.keys():
            self.Q[state] = {}
        self.Q[state][action] = (1-self.alpha)*self.getQValue(state,action) + self.alpha*(reward + self.discount*maxQ)
        """
        self.Q[state,action] = (1-self.alpha)*self.getQValue(state,action) + self.alpha*(reward + self.discount*self.getValue(nextState))
    
    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)


class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1

        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = QLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action
