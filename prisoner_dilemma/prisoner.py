import random

'''
Your Prisoner class. This class gets created every time a match with another Prisoner begins. An instance will exist only for a match with one Prisoner.
After a match with another Prisoner ends, this class gets destroyed - i.e. you cannot store any data between matches.

For every pair of teams we create your and the other team's prisoner. You will play a large number of games, where for each game we call 'talk' on your prisoner 
and the other team's. We then call 'getResult' on your and the other team's prisoners with the game results.
'''
class Prisoner:
    
    '''
    Init function gets called when your Prisoner instance gets created. Create any data structures here.
    '''
    def __init__(self):
        ##contructor##
        print("Creating Prisoner")    
    
    '''
    talk() is called every time a single game of the dilemma is played and is expected to return 'True' or 'False' boolean values.
    '''
    def talk(self):
        return random.choice([True, False])
    
    '''
    getResult() is called at the end of a single game of the dilemma, and you will receive a single integer {-3,-2,-1,0} representing your score.
    '''
    def getResult(self, result):
        print(result)
