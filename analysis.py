# analysis.py
# -----------
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


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question3():
    answerEpsilon = 0
    answerLearningRate = 1
    return answerEpsilon, answerLearningRate
    # If not possible, return 'NOT POSSIBLE'
    
def question3_1():
    answerEpsilon = 0.1
    answerLearningRate = 1
    return answerEpsilon, answerLearningRate

def question3_2():
    answerEpsilon = 0.1
    answerLearningRate = 0.9
    return answerEpsilon, answerLearningRate

def question3_3():
    answerEpsilon = 0.2
    answerLearningRate = 0.9
    return answerEpsilon, answerLearningRate

def question3_4():
    answerEpsilon = 1
    answerLearningRate = 0
    return answerEpsilon, answerLearningRate

def question3_5():
    answerEpsilon = 1
    answerLearningRate = 0.1
    return answerEpsilon, answerLearningRate

def question3_6():
    answerEpsilon = 0.9
    answerLearningRate = 0.1
    return answerEpsilon, answerLearningRate

def question3_7():
    answerEpsilon = 0.9
    answerLearningRate = 0.2
    return answerEpsilon, answerLearningRate

def question3_8():
    answerEpsilon = 0.5
    answerLearningRate = 0.5
    return answerEpsilon, answerLearningRate

def question3_9():
    return 'NOT POSSIBLE'

if __name__ == '__main__':
    print 'Answers to analysis questions:'
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print '  Question %s:\t%s' % (q, str(response))
